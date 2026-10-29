import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

export interface Response<T> {
  statusCode: number;
  success: boolean;
  message: string;
  data: T;
  meta?: any;
}

@Injectable()
export class TransformResponseInterceptor<T>
  implements NestInterceptor<T, Response<T>>
{
  intercept(
    context: ExecutionContext,
    next: CallHandler,
  ): Observable<Response<T>> {
    const ctx = context.switchToHttp();
    const response = ctx.getResponse();
    const statusCode = response.statusCode;

    return next.handle().pipe(
      map((result) => {
        // If result already has custom structure (e.g., paginated)
        if (result && typeof result === 'object' && 'data' in result && 'meta' in result) {
          return {
            statusCode,
            success: true,
            message: result.message || 'Permintaan berhasil diproses',
            data: result.data,
            meta: result.meta,
          };
        }

        return {
          statusCode,
          success: true,
          message: (result && result.message) || 'Permintaan berhasil diproses',
          data: result && 'data' in result ? result.data : result,
        };
      }),
    );
  }
}

