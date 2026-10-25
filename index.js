import { Client, GatewayDispatchEvents } from '@discordjs/core';
import { REST } from '@discordjs/rest';
import { WebSocketManager } from '@discordjs/ws';

const token = process.env.MICUP_BOT_TOKEN;

if (!token) {
  console.error('❌ MICUP_BOT_TOKEN bulunamadı! Secrets kısmını kontrol et.');
  process.exit(1);
}

const API_BASE = 'https://micup.gg';

const rest = new REST({ api: API_BASE, version: '1' }).setToken(token);

const gateway = new WebSocketManager({
  token,
  intents: 0,
  rest,
  version: '1',
});

const client = new Client({ rest, gateway });

client.on(GatewayDispatchEvents.Ready, (data) => {
  console.log(`✅ Giriş yapıldı: ${data.user.username}`);
});

gateway.connect().catch((err) => {
  console.error('❌ Bağlantı hatası:', err);
});
