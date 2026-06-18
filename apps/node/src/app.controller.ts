import { Controller, Get, Header, Param, ParseIntPipe } from '@nestjs/common';

const appName = process.env.APP_NAME ?? 'N/A';

@Controller()
export class AppController {
  @Get()
  @Header('served_by', appName)
  root() {
    return { message: 'Hello from NestJS!' };
  }

  @Get('api/health')
  @Header('served_by', appName)
  health() {
    return { status: 'healthy' };
  }

  @Get('api/items/:itemId')
  @Header('served_by', appName)
  readItem(@Param('itemId', ParseIntPipe) itemId: number) {
    return { item_id: itemId, name: `Item ${itemId}` };
  }
}
