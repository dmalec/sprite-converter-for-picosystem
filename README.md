# sprite-converter-for-picosystem
A small utility to convert images into sprites for Pimoroni's PicoSystem SDK

# Setting up the Environment
```commandline
git clone git@github.com:dmalec/sprite-converter-for-picosystem.git
cd sprite-converter-for-picosystem
python3 -m venv venv
```

On Mac/Linux:
```commandline
source venv/bin/activate
```

On Windows:
```commandline
venv\Scripts\activate.bat
```

All systems (inside the `venv` python environment started just above):
```commandline
python -m pip install -r requirements.txt
deactivate
```

# Running
From the `sprite-converter-for-picosystem` directory do the following.

On Mac/Linux:
```commandline
source venv/bin/activate
```

On Windows:
```commandline
venv\Scripts\activate.bat
```

All systems (inside the `venv` python environment started just above):
```commandline
python sprite_converter.py demo_image.png 
```

This should produce output like the following:
```c
// Custom sprite sheet
const color_t custom_sprite_sheet_data[256] = {
  0x00ff, 0x00ff, 0x00ff, 0x00ff, 0x00ff, 0x00ff, 0x00ff, 0x00ff,
  0x0000, 0x0000, 0x0000, 0xf0f0, 0xf0f0, 0x0000, 0x0000, 0x0000,
...
  0x0000, 0x0000, 0x0000, 0x0ff0, 0x0ff0, 0x0000, 0x0000, 0x0000,
  0x00f0, 0x00f0, 0xffff, 0xffff, 0x00f0, 0x00f0, 0xffff, 0xffff,
};
buffer_t CUSTOM_SPRITESHEET{.w = 16, .h = 16,.data = (color_t *)custom_sprite_sheet_data};
buffer_t *custom_sprite_sheet = &CUSTOM_SPRITESHEET;
```

Which can then be pasted into your source code and used like so:
```c
  // load custom spritesheet
  spritesheet(*custom_sprite_sheet);
...
  // draw the first sprite at location 10, 20
  sprite(0, 10, 20);

