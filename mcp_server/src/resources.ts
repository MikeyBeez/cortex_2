export const RESOURCES = [
  {
    uri: 'cortex://modules/catalog',
    name: 'Module Catalog',
    description: 'Browse all available cognitive modules with their metadata',
    mimeType: 'application/json',
  },
  {
    uri: 'cortex://state/current',
    name: 'Current State',
    description: 'Current system state including loaded modules, identity, and context',
    mimeType: 'application/json',
  },
  {
    uri: 'cortex://metrics/learning',
    name: 'Learning Metrics',
    description: 'Learning system performance metrics and patterns',
    mimeType: 'application/json',
  },
];
