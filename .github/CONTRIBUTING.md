# Contributing to Spooler Docs

## Quick edits

For small fixes (typos, corrections), click **Edit this page** directly in the docs site — it opens GitHub's editor and creates a PR automatically.

## Larger changes

1. Clone the repo
2. Install Mintlify CLI: `npm install -g mintlify`
3. Run `mintlify dev` and open http://localhost:3000
4. Edit `.mdx` files — the preview hot-reloads
5. Open a PR against `main`

## Adding a new page

1. Create a `.mdx` file in the appropriate folder
2. Add it to the `navigation` array in `mint.json`
3. Use existing pages as templates for formatting

## MDX components

Mintlify provides these components out of the box:

- `<Card>`, `<CardGroup>` — feature cards
- `<Steps>`, `<Step>` — numbered steps
- `<Tabs>`, `<Tab>` — tabbed content
- `<Info>`, `<Warning>`, `<Tip>`, `<Check>` — callouts
- `<Accordion>`, `<AccordionGroup>` — collapsible sections

Full reference: https://mintlify.com/docs/components
