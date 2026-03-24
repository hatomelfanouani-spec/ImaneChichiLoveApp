"""
Generate PWA icons for Imane Love App
Creates heart-themed PNG icons at all required sizes
"""
import os
import math

def create_svg_icon(size):
    """Create a beautiful heart icon as SVG, then describe it"""
    # We'll create the icon programmatically
    cx, cy = size // 2, size // 2

    # Heart path math
    # Using a standard heart parametric equation
    def heart_point(t, scale, ox, oy):
        x = scale * 16 * (math.sin(t) ** 3)
        y = -scale * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        return ox + x, oy + y

    scale = size * 0.032
    points = []
    for i in range(64):
        t = (i / 64) * 2 * math.pi
        px, py = heart_point(t, scale, cx, cy - size * 0.02)
        points.append(f"{px:.1f},{py:.1f}")

    polygon = " ".join(points)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2a0a3e"/>
      <stop offset="100%" stop-color="#0d0518"/>
    </radialGradient>
    <radialGradient id="heart" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#f0c8d8"/>
      <stop offset="50%" stop-color="#e8a4b8"/>
      <stop offset="100%" stop-color="#c97a9a"/>
    </radialGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="{size*0.02}" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="{size}" height="{size}" rx="{size*0.22}" fill="url(#bg)"/>
  <!-- Glow -->
  <ellipse cx="{cx}" cy="{cy}" rx="{size*0.35}" ry="{size*0.3}" fill="rgba(232,164,184,0.15)"/>
  <!-- Heart -->
  <polygon points="{polygon}" fill="url(#heart)" filter="url(#glow)"/>
  <!-- Sparkles -->
  <text x="{size*0.2}" y="{size*0.25}" font-size="{size*0.12}" opacity="0.8">✦</text>
  <text x="{size*0.72}" y="{size*0.3}" font-size="{size*0.1}" opacity="0.6">✦</text>
</svg>'''
    return svg


def write_svg_as_placeholder(path, size):
    """Write SVG icon to file"""
    svg_content = create_svg_icon(size)
    with open(path.replace('.png', '.svg'), 'w') as f:
        f.write(svg_content)


os.makedirs('icons', exist_ok=True)

sizes = [72, 96, 128, 144, 192, 512]

# Try to use PIL if available, otherwise create SVG placeholders
try:
    from PIL import Image, ImageDraw, ImageFont
    import struct, zlib

    def create_png_icon(size):
        """Create a PNG icon with PIL"""
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Background with rounded corners
        bg_color = (26, 10, 46, 255)
        radius = int(size * 0.22)

        # Draw rounded rectangle background
        draw.rounded_rectangle([0, 0, size-1, size-1], radius=radius, fill=bg_color)

        # Draw heart using bezier-ish approach
        cx, cy = size // 2, size // 2

        # Simple heart with two circles + triangle
        r = int(size * 0.22)
        # Left circle
        draw.ellipse([cx - r*2, cy - r, cx, cy + r//2], fill=(232, 164, 184, 240))
        # Right circle
        draw.ellipse([cx, cy - r, cx + r*2, cy + r//2], fill=(232, 164, 184, 240))
        # Bottom triangle
        draw.polygon([
            (cx - r*2 + 2, cy + r//3),
            (cx + r*2 - 2, cy + r//3),
            (cx, cy + r*2),
        ], fill=(232, 164, 184, 240))

        return img

    for sz in sizes:
        img = create_png_icon(sz)
        img.save(f'icons/icon-{sz}.png', 'PNG')
        print(f'Created icons/icon-{sz}.png')

    print('✅ All PNG icons created with PIL!')

except ImportError:
    # Fallback: write SVG icons + tiny valid PNG using raw bytes
    print('PIL not available, creating SVG icons + minimal PNGs...')

    for sz in sizes:
        # Write SVG
        svg_path = f'icons/icon-{sz}.svg'
        write_svg_as_placeholder(f'icons/icon-{sz}.png', sz)
        print(f'Created SVG: {svg_path}')

    # Create a minimal valid 1x1 pink PNG and copy it (as placeholder)
    # Valid minimal PNG bytes
    def create_minimal_png(color_r, color_g, color_b):
        """Generate a valid minimal 1x1 PNG"""
        def png_chunk(chunk_type, data):
            chunk_len = struct.pack('>I', len(data))
            chunk_data = chunk_type + data
            chunk_crc = struct.pack('>I', zlib.crc32(chunk_data) & 0xffffffff)
            return chunk_len + chunk_data + chunk_crc

        signature = b'\x89PNG\r\n\x1a\n'
        ihdr_data = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)
        ihdr = png_chunk(b'IHDR', ihdr_data)

        raw_data = b'\x00' + bytes([color_r, color_g, color_b])
        compressed = zlib.compress(raw_data)
        idat = png_chunk(b'IDAT', compressed)
        iend = png_chunk(b'IEND', b'')

        return signature + ihdr + idat + iend

    pink_png = create_minimal_png(232, 164, 184)
    for sz in sizes:
        with open(f'icons/icon-{sz}.png', 'wb') as f:
            f.write(pink_png)
        print(f'Created placeholder PNG: icons/icon-{sz}.png')

    print('✅ Placeholder icons created! Replace with real icons for production.')

print('\n📱 Icons ready! Place them in the app folder alongside index.html.')
