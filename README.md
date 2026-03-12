# Spooler Documentation

User documentation for the Spooler cable measurement system, built with [Mintlify](https://mintlify.com).

**Live docs:** https://docs.spooler.cz

## Structure

```
├── hardware/          # Spooler device — installation, display, BLE
├── mobile-app/        # iOS/Android app — pairing, measurement, sync
├── web-app/           # Web dashboard — spools, projects, reports
├── introduction.mdx   # System overview
├── quickstart.mdx     # Getting started in 10 minutes
└── mint.json          # Mintlify configuration
```

## Local preview

```bash
npm install -g mintlify
mintlify dev
```

Open http://localhost:3000

## Contributing

1. Edit `.mdx` files in the relevant section
2. Preview locally with `mintlify dev`
3. Open a PR — Mintlify auto-deploys on merge to `main`

## Links

- Web app: https://app.spooler.cz
- Main repo: https://github.com/snailrollers/claud
- Mobile app: https://github.com/snailrollers/spooler-flu
