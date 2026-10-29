import zipfile
import xml.etree.ElementTree as ET
import re
import json
import os

DOCX_PATH = 'Resep Masakan Indonesia & Internasional.docx'
OUTPUT_PATH = 'src/seeder/recipes-data.json'

def get_paragraphs(docx_path):
    z = zipfile.ZipFile(docx_path)
    tree = ET.fromstring(z.read('word/document.xml'))
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paragraphs = []
    for p in tree.findall('.//w:p', namespaces):
        t_nodes = p.findall('.//w:t', namespaces)
        if t_nodes:
            txt = ''.join([t.text for t in t_nodes if t.text]).strip()
            if txt:
                paragraphs.append(txt)
    return paragraphs

def create_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text).strip('-')
    return text

def parse_ingredient_line(raw_line):
    unit_pattern = r'(?:kg|g|gram|liter|ml|siung|butir|buah|batang|lembar|sdm|sdt|ekor|porsi|cm|ruas|tangkai|mangkok|bungkus|papan|ikat)'
    
    amount = None
    unit = None
    name = raw_line
    notes = None
    
    # Extract notes in parentheses
    m_notes = re.search(r'\(([^)]+)\)$', raw_line)
    if m_notes:
        notes = m_notes.group(1).strip()
        name = raw_line[:m_notes.start()].strip()
        
    m_qty = re.match(r'^([\d\/\.,]+)\s*(' + unit_pattern + r')?\b\s*(.*)', name, re.IGNORECASE)
    if m_qty:
        amount_str = m_qty.group(1).strip()
        # Convert fractions if any (e.g. 1/2 -> 0.5)
        if '/' in amount_str:
            try:
                num, denom = amount_str.split('/')
                amount = round(float(num) / float(denom), 2)
            except:
                amount = None
        else:
            try:
                amount = float(amount_str.replace(',', '.'))
            except:
                amount = None
        unit = m_qty.group(2)
        name = m_qty.group(3).strip()
    elif 'secukupnya' in name.lower():
        unit = 'secukupnya'
        name = re.sub(r'\bsecukupnya\b', '', name, flags=re.IGNORECASE).strip()
        
    return {
        'rawText': raw_line,
        'amount': amount,
        'unit': unit,
        'name': name,
        'notes': notes
    }

def infer_category(title, ingredients_text):
    lower_t = title.lower()
    lower_i = ingredients_text.lower()
    
    if any(k in lower_t for k in ['soto', 'sup', 'coto', 'rawon', 'sayur lodeh', 'sayur asem', 'tom yum', 'pindang']):
        return 'Sup & Soto', 'sup-soto', 'Aneka masakan berkuah, soto nusantara, dan sup hangat kaya rempah'
    if any(k in lower_t for k in ['sate', 'bakar', 'panggang']):
        return 'Sate & Bakaran', 'sate-bakaran', 'Aneka hidangan sate, daging, dan ikan bakar aroma asap'
    if any(k in lower_t for k in ['es ', 'dawet', 'cendol', 'minuman']):
        return 'Minuman Segar', 'minuman-segar', 'Minuman tradisional segar pelepas dahaga'
    if any(k in lower_t for k in ['klepon', 'onde', 'nagasari', 'lemper', 'dadar gulung', 'martabak manis', 'terang bulan', 'kue', 'tteokbokki']):
        return 'Kudapan & Jajanan Pasar', 'kudapan-jajanan-pasar', 'Kue tradisional, camilan, dan jajanan pasar populer'
    if any(k in lower_t for k in ['mie ', 'mi ', 'pasta', 'spaghetti', 'lasagna', 'pad thai', 'bihun', 'kwetiau']):
        return 'Mi & Pasta', 'mi-pasta', 'Olahan mi nusantara dan pasta internasional'
    if any(k in lower_t for k in ['nasi ', 'bibimbap', 'tumpeng', 'kimbap', 'sushi']):
        return 'Nasi & Olahan Beras', 'nasi-olahan-beras', 'Hidangan nasi spesial dan olahan beras khas'
    if any(k in lower_t for k in ['gado-gado', 'karedok', 'urap', 'pecel', 'tumis', 'capcay', 'sayur']):
        return 'Sayuran & Tumisan', 'sayuran-tumisan', 'Aneka sajian sayuran segar dan tumisan sehat'
    if any(k in lower_t for k in ['ayam', 'bebek', 'unggas', 'chicken']):
        return 'Ayam & Unggas', 'ayam-unggas', 'Olahan daging ayam dan unggas dengan berbagai bumbu'
    if any(k in lower_t for k in ['ikan', 'udang', 'tenggiri', 'patin', 'seafood', 'kakap', 'gurame', 'crab']):
        return 'Ikan & Seafood', 'ikan-seafood', 'Hidangan olahan ikan laut/tawar dan hidangan laut segar'
    if any(k in lower_t for k in ['daging', 'sapi', 'kambing', 'iga', 'buntut', 'rendang', 'empal', 'semur', 'kikil', 'kebab', 'burger', 'bulgogi']):
        return 'Daging Sapi & Kambing', 'daging-sapi-kambing', 'Masakan berbahan dasar daging sapi, kambing, dan olahannya'
    
    # Check ingredient text
    if 'daging sapi' in lower_i or 'daging kambing' in lower_i:
        return 'Daging Sapi & Kambing', 'daging-sapi-kambing', 'Masakan berbahan dasar daging sapi, kambing, dan olahannya'
    if 'ayam' in lower_i:
        return 'Ayam & Unggas', 'ayam-unggas', 'Olahan daging ayam dan unggas dengan berbagai bumbu'
    if 'ikan' in lower_i or 'udang' in lower_i:
        return 'Ikan & Seafood', 'ikan-seafood', 'Hidangan olahan ikan laut/tawar dan hidangan laut segar'
        
    return 'Lauk Utama Nusantara', 'lauk-utama-nusantara', 'Pilihan lauk utama lezat pendamping nasi'

def infer_cuisine_type(number, title, origin):
    lower_t = title.lower()
    
    if number > 150:
        if any(c in (origin or '').lower() for c in ['jepang', 'korea', 'singapura', 'thailand', 'tiongkok']):
            return 'Asian Cuisine', 'asian-cuisine', 'Kuliner populer dari berbagai negara Asia'
        return 'Western & International', 'western-international', 'Masakan internasional, barat, dan eropa'
        
    if any(k in lower_t for k in ['lebaran', 'tumpeng']):
        return 'Hari Raya & Perayaan', 'hari-raya-perayaan', 'Hidangan spesial hari raya dan perayaan tradisi'
    if any(k in lower_t for k in ['kampung', 'rumahan', 'lodeh', 'sayur asem', 'sayur bening', 'tempe', 'tahu']):
        return 'Masakan Rumahan', 'masakan-rumahan', 'Masakan praktis dan lezat sehari-hari keluarga di rumah'
    if any(k in lower_t for k in ['gila', 'pempek', 'siomay', 'bakso', 'ketoprak', 'kaki lima']):
        return 'Street Food & Kaki Lima', 'street-food-kaki-lima', 'Jajanan dan kuliner jalanan legendaris kaki lima'
    if any(k in lower_t for k in ['klepon', 'onde', 'nagasari', 'lemper', 'dadar gulung', 'martabak', 'dawet', 'es ']):
        return 'Kudapan & Minuman Tradisional', 'kudapan-minuman-tradisional', 'Jajanan pasar, kue basah, dan minuman segar tradisi'
        
    return 'Masakan Daerah Tradisional', 'masakan-daerah-tradisional', 'Kuliner autentik khas berbagai daerah di Indonesia'

def infer_origin(full_name):
    m_orig = re.search(r'\(([^)]+)\)$', full_name)
    if m_orig:
        return m_orig.group(1).strip()
    
    # Infer from title
    known_regions = {
        'Jawa Tengah': 'Jawa Tengah',
        'Jawa Timur': 'Jawa Timur',
        'Jawa Barat': 'Jawa Barat',
        'Surabaya': 'Surabaya, Jawa Timur',
        'Malang': 'Malang, Jawa Timur',
        'Madura': 'Madura, Jawa Timur',
        'Jogja': 'DI Yogyakarta',
        'Yogyakarta': 'DI Yogyakarta',
        'Jakarta': 'DKI Jakarta',
        'Betawi': 'DKI Jakarta',
        'Bali': 'Bali',
        'Jawa': 'Jawa',
        'Kampung': 'Nusantara',
        'Lebaran': 'Nusantara'
    }
    for k, v in known_regions.items():
        if k.lower() in full_name.lower():
            return v
    return 'Indonesia'

def infer_prep_cook_time(steps_text):
    cook_time = 30
    prep_time = 20
    
    # Check hours
    m_hour = re.search(r'(\d+)(?:\s*[-–]\s*(\d+))?\s*jam', steps_text, re.IGNORECASE)
    if m_hour:
        h1 = int(m_hour.group(1))
        h2 = int(m_hour.group(2)) if m_hour.group(2) else h1
        cook_time = int(((h1 + h2) / 2) * 60)
    else:
        # Check minutes
        m_min = re.search(r'(\d+)(?:\s*[-–]\s*(\d+))?\s*menit', steps_text, re.IGNORECASE)
        if m_min:
            m1 = int(m_min.group(1))
            m2 = int(m_min.group(2)) if m_min.group(2) else m1
            cook_time = int((m1 + m2) / 2)
            
    if cook_time > 60:
        prep_time = 30
    elif cook_time < 20:
        prep_time = 15
        
    return prep_time, cook_time

def infer_difficulty(cook_time, num_steps, num_ingredients):
    if cook_time >= 120 or (num_steps >= 5 and num_ingredients >= 15):
        return 'HARD'
    if cook_time <= 25 and num_steps <= 3:
        return 'EASY'
    return 'MEDIUM'

def infer_spiciness(ingredients_text, title):
    lower = (ingredients_text + ' ' + title).lower()
    rawit_count = 0
    m_rawit = re.search(r'(\d+)\s*(?:buah|biji)\s*cabai rawit', lower)
    if m_rawit:
        rawit_count = int(m_rawit.group(1))
        
    if 'mercon' in lower or 'pedas' in lower or rawit_count >= 10:
        return 3
    if 'cabai' in lower or 'sambal' in lower or 'balado' in lower or rawit_count >= 3:
        return 2
    if 'lada' in lower or 'merica' in lower or 'jahe' in lower or 'rawit' in lower:
        return 1
    return 0

def main():
    paragraphs = get_paragraphs(DOCX_PATH)
    recipe_indices = [i for i, p in enumerate(paragraphs) if re.match(r'^\d+\.\s+', p)]
    print(f'Detected {len(recipe_indices)} recipes in {DOCX_PATH}')

    recipes = []
    categories_set = {}
    cuisine_types_set = {}

    for idx, r_idx in enumerate(recipe_indices):
        next_idx = recipe_indices[idx+1] if idx+1 < len(recipe_indices) else len(paragraphs)
        lines = paragraphs[r_idx:next_idx]
        
        title_line = lines[0]
        m_num = re.match(r'^(\d+)\.\s*(.*)', title_line)
        recipe_no = int(m_num.group(1))
        full_name = m_num.group(2).strip()
        
        origin = infer_origin(full_name)
        clean_name = full_name
        m_orig = re.search(r'\(([^)]+)\)$', full_name)
        if m_orig:
            clean_name = full_name[:m_orig.start()].strip()
            
        slug = f"{create_slug(clean_name)}-{recipe_no}" if recipe_no in [14, 18] else create_slug(clean_name)
        scope = 'INDONESIA' if recipe_no <= 150 else 'INTERNATIONAL'
        
        visual_ref = None
        ingredient_groups = []
        steps = []
        nutrition = None
        
        current_sec = None
        current_grp = None
        
        all_ingredients_text = []
        all_steps_text = []
        
        for line in lines[1:]:
            if line.startswith('Referensi Visual:'):
                visual_ref = line.replace('Referensi Visual:', '').strip()
                continue
            if line.startswith('Deskripsi Bahan Baku:'):
                current_sec = 'BAHAN'
                continue
            if line.startswith('Langkah-Langkah Pembuatan:'):
                current_sec = 'LANGKAH'
                continue
            if line.startswith('Nutrisi'):
                current_sec = 'NUTRISI'
                nutrition = {'rawText': line, 'serving': None, 'calories': None, 'protein': None, 'fat': None, 'carbohydrates': None, 'notes': None}
                
                m_serv = re.search(r'Nutrisi\s*(?:\((.*?)\))?:', line)
                if m_serv and m_serv.group(1):
                    nutrition['serving'] = m_serv.group(1).strip()
                
                cal = re.search(r'Kalori\s*(\d+)', line)
                prot = re.search(r'Protein\s*(\d+(?:\.\d+)?)', line)
                fat = re.search(r'Lemak\s*(\d+(?:\.\d+)?)', line)
                carb = re.search(r'Karbohidrat\s*(\d+(?:\.\d+)?)', line)
                
                if cal: nutrition['calories'] = int(cal.group(1))
                if prot: nutrition['protein'] = float(prot.group(1))
                if fat: nutrition['fat'] = float(fat.group(1))
                if carb: nutrition['carbohydrates'] = float(carb.group(1))
                
                # notes
                if '.' in line:
                    notes_part = line.split('.', 1)[1].strip()
                    if notes_part:
                        nutrition['notes'] = notes_part
                continue
                
            if current_sec == 'BAHAN':
                all_ingredients_text.append(line)
                if line.endswith(':'):
                    current_grp = {
                        'name': line[:-1].strip(),
                        'orderIndex': len(ingredient_groups) + 1,
                        'ingredients': []
                    }
                    ingredient_groups.append(current_grp)
                else:
                    if current_grp is None:
                        current_grp = {
                            'name': 'Bahan Utama',
                            'orderIndex': len(ingredient_groups) + 1,
                            'ingredients': []
                        }
                        ingredient_groups.append(current_grp)
                    parsed_item = parse_ingredient_line(line)
                    parsed_item['orderIndex'] = len(current_grp['ingredients']) + 1
                    current_grp['ingredients'].append(parsed_item)
            elif current_sec == 'LANGKAH':
                all_steps_text.append(line)
                step_no = len(steps) + 1
                if ':' in line and not line.startswith('http'):
                    parts = line.split(':', 1)
                    steps.append({
                        'stepNumber': step_no,
                        'title': parts[0].strip(),
                        'instruction': parts[1].strip(),
                        'rawText': line
                    })
                else:
                    steps.append({
                        'stepNumber': step_no,
                        'title': None,
                        'instruction': line,
                        'rawText': line
                    })

        ingredients_str = ' '.join(all_ingredients_text)
        steps_str = ' '.join(all_steps_text)
        
        cat_name, cat_slug, cat_desc = infer_category(clean_name, ingredients_str)
        categories_set[cat_slug] = {'name': cat_name, 'slug': cat_slug, 'description': cat_desc}
        
        type_name, type_slug, type_desc = infer_cuisine_type(recipe_no, clean_name, origin)
        cuisine_types_set[type_slug] = {'name': type_name, 'slug': type_slug, 'description': type_desc}
        
        prep_time, cook_time = infer_prep_cook_time(steps_str)
        difficulty = infer_difficulty(cook_time, len(steps), sum(len(g['ingredients']) for g in ingredient_groups))
        spiciness = infer_spiciness(ingredients_str, clean_name)
        
        recipes.append({
            'recipeNumber': recipe_no,
            'title': title_line,
            'name': clean_name,
            'slug': slug,
            'scope': scope,
            'origin': origin,
            'visualRef': visual_ref,
            'imageUrl': None,
            'prepTimeMinutes': prep_time,
            'cookTimeMinutes': cook_time,
            'servings': 4,
            'difficulty': difficulty,
            'spicinessLevel': spiciness,
            'categorySlug': cat_slug,
            'cuisineTypeSlug': type_slug,
            'rawContent': '\n'.join(lines),
            'ingredientGroups': ingredient_groups,
            'steps': steps,
            'nutrition': nutrition
        })

    # Ensure unique slugs
    seen_slugs = set()
    for r in recipes:
        original_slug = r['slug']
        suffix = 1
        while r['slug'] in seen_slugs:
            r['slug'] = f"{original_slug}-{suffix}"
            suffix += 1
        seen_slugs.add(r['slug'])

    output_data = {
        'categories': list(categories_set.values()),
        'cuisineTypes': list(cuisine_types_set.values()),
        'recipes': recipes
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f'Successfully exported {len(recipes)} recipes, {len(categories_set)} categories, and {len(cuisine_types_set)} cuisine types to {OUTPUT_PATH}')

if __name__ == '__main__':
    main()

