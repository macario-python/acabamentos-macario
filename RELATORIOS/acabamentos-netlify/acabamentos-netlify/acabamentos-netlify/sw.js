const CACHE = 'acabamentos-v1';
const ASSETS = [
  '/login.html',
  '/index.html',
  '/manifest.json'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  // Sempre busca da rede primeiro (dados do Supabase precisam ser frescos)
  e.respondWith(
    fetch(e.request).catch(() => caches.match(e.request))
  );
});
