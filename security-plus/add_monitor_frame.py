import re

with open('domain-3.html', 'r') as f:
    html = f.read()

styles = """
        <style>
            .monitor-frame {
                background: #000;
                padding: 1.5rem 1.5rem 3rem 1.5rem;
                border-radius: 20px;
                box-shadow: 0 24px 48px rgba(0,0,0,0.8), inset 0 2px 4px rgba(255,255,255,0.1);
                position: relative;
                border: 2px solid #27272a;
                margin-bottom: 0;
            }
            .monitor-frame::before {
                content: '';
                position: absolute;
                top: 0.75rem;
                left: 50%;
                transform: translateX(-50%);
                width: 6px;
                height: 6px;
                background: #111;
                border-radius: 50%;
                box-shadow: inset 0 1px 2px rgba(0,0,0,0.5);
            }
            .monitor-stand {
                width: 120px;
                height: 40px;
                background: linear-gradient(to bottom, #27272a, #18181b);
                margin: 0 auto;
                box-shadow: inset 0 2px 5px rgba(0,0,0,0.5);
            }
            .monitor-base {
                width: 260px;
                height: 12px;
                background: #3f3f46;
                margin: 0 auto 2.5rem auto;
                border-radius: 4px 4px 0 0;
                box-shadow: 0 5px 15px rgba(0,0,0,0.6);
            }
            .canvas-element {
                width: 100%;
                height: auto;
                display: block;
                margin: 0 auto;
                background-color: var(--bg-surface-elevated);
                border: 1px solid var(--border-subtle);
                border-radius: 4px;
            }
            .sim-controls {
                display: flex;
                flex-direction: row;
                justify-content: center;
                gap: 1.5rem;
                margin-bottom: 2rem;
            }
            .sim-controls .button {
                padding: 0.8rem 1.5rem;
                border-radius: var(--radius-md);
                font-weight: 600;
                cursor: pointer;
                transition: all var(--transition-fast);
                font-family: inherit;
                font-size: 1rem;
            }
            .btn-vulnerable {
                background: rgba(153, 27, 27, 0.15);
                color: #fca5a5;
                border: 1px solid rgba(153, 27, 27, 0.3);
            }
            .btn-vulnerable:hover {
                background: rgba(153, 27, 27, 0.3);
                border-color: rgba(153, 27, 27, 0.5);
                color: #fecaca;
                transform: translateY(-2px);
            }
            .btn-secured {
                background: rgba(22, 101, 52, 0.15);
                color: #86efac;
                border: 1px solid rgba(22, 101, 52, 0.3);
            }
            .btn-secured:hover {
                background: rgba(22, 101, 52, 0.3);
                border-color: rgba(22, 101, 52, 0.5);
                color: #bbf7d0;
                transform: translateY(-2px);
            }
            .status-panel {
                text-align: center;
                padding: 1rem;
                background-color: var(--bg-surface-elevated);
                border-radius: var(--radius-md);
                border: 1px solid var(--border-strong);
                min-height: 5rem;
                display: flex;
                align-items: center;
                justify-content: center;
                color: var(--text-primary);
            }
        </style>
"""

# Insert styles before the sim-wrapper
html = html.replace('<div class="sim-wrapper">', styles + '\n      <div class="sim-wrapper">')

# Wrap the canvas
old_canvas = """        <div class="aspect-video">
            <canvas id="simCanvas" width="800" height="450" class="canvas-element"></canvas>
        </div>"""

new_canvas = """        <div class="monitor-frame">
            <div class="aspect-video">
                <canvas id="simCanvas" width="800" height="450" class="canvas-element"></canvas>
            </div>
        </div>
        <div class="monitor-stand"></div>
        <div class="monitor-base"></div>"""

html = html.replace(old_canvas, new_canvas)

with open('domain-3.html', 'w') as f:
    f.write(html)

print("Added monitor border and fixed button styles.")
