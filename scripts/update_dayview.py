import sys
fpath = r'D:\Projects\Placement_Master_Handbook_Web\js\views\dayView.js'
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add import
import_stmt = "import { renderSvgDiagram } from '../diagrams.js';"
new_import = "import { renderSvgDiagram } from '../diagrams.js';\nimport { renderDsaVisualizer, attachVisualizerInteractivity } from '../visualizers.js';"
content = content.replace(import_stmt, new_import)

# Replace the static SVG diagram with the new visualizer
old_svg_block = """      ${dsaPattern.visual_explanation ? `
        <div style="margin: var(--space-4) 0;">
          <h4 style="margin-bottom: var(--space-2); color: var(--color-primary); display: flex; align-items: center; justify-content: space-between;">
            <span>Visual Execution Trace & Pointer Mechanics</span>
            <span class="badge badge-success">Algorithm Visualizer</span>
          </h4>
          ${renderSvgDiagram(dsaPattern.pattern_name || '', dsaPattern.visual_explanation)}
        </div>
      ` : ''}"""

new_svg_block = """      ${dsaPattern.pattern_name ? `
        <div style="margin: var(--space-4) 0;">
          <h4 style="margin-bottom: var(--space-2); color: var(--color-primary); display: flex; align-items: center; justify-content: space-between;">
            <span>Interactive Animated Execution Trace</span>
          </h4>
          ${renderDsaVisualizer(dsaPattern, dsaPattern.java_code || dsaPattern.java_solution || dsaPattern.code || '')}
        </div>
      ` : ''}"""

if old_svg_block in content:
    content = content.replace(old_svg_block, new_svg_block)
    print('Replaced SVG block')
else:
    print('Could not find SVG block')

# Inject attachVisualizerInteractivity
attach_stmt = "  // Checkbox bindings & persistence"
new_attach = "  // Initialize DSA visualizer\n  attachVisualizerInteractivity(container);\n\n  // Checkbox bindings & persistence"
if attach_stmt in content:
    content = content.replace(attach_stmt, new_attach)
    print('Replaced attach statement')
else:
    print('Could not find attach statement')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated dayView.js')
