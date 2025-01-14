## MODEL

MODEL_DATA = {
    # Общие модели
    "Stable Diffusion XL Base": {
        "url": "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors",
        "filename": "sd_xl_base_1.0.safetensors"
    },
    "Stable Diffusion v1.5": {
        "url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors",
        "filename": "v1-5-pruned.safetensors"
    },
    
    # Реалистичные модели
    "Realistic Vision V5.1": {
        "url": "https://civitai.com/api/download/models/130072",
        "filename": "realisticVisionV51.safetensors"
    },
    "PhotonV1": {
        "url": "https://civitai.com/api/download/models/63977",
        "filename": "photon_v1.safetensors"
    },

    # Аниме модели
    "AnythingV5": {
        "url": "https://civitai.com/api/download/models/90854",
        "filename": "anythingV5_v5.safetensors"
    },
    "CounterfeitV30": {
        "url": "https://civitai.com/api/download/models/57618",
        "filename": "counterfeitV30.safetensors"
    },

    # Стилизованные модели
    "Deliberate v3": {
        "url": "https://civitai.com/api/download/models/15236",
        "filename": "deliberate_v3.safetensors"
    },
    "RevAnimated v122": {
        "url": "https://civitai.com/api/download/models/46846",
        "filename": "revAnimated_v122.safetensors"
    }
    # ... добавьте другие модели по аналогии
}

## VAE

vae_list = {
    "1. ae": [
      {"url": "https://huggingface.co/UmeAiRT/ComfyUI-Auto_installer/resolve/main/models/vae/ae.safetensors", "name": "ae"},
    ],
    "2. Anything.vae": [{"url": "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/anything_fp16.safetensors", "name": "Anything.vae.safetensors"}],
    "3. Blessed2.vae": [{"url": "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/blessed2_fp16.safetensors", "name": "Blessed2.vae.safetensors"}],
    "4. ClearVae.vae": [{"url": "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/ClearVAE_V2.3_fp16.safetensors", "name": "ClearVae_23.vae.safetensors"}],
    "5. WD.vae": [{"url": "https://huggingface.co/NoCrypt/resources/resolve/main/VAE/wd.vae.safetensors", "name": "WD.vae.safetensors"}]
}

## CONTROLNET

controlnet_list = {
    "1. Openpose": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_openpose_fp16.yaml"}
    ],
    "2. Canny": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_canny_fp16.yaml"}
    ],
    "3. Depth": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1p_sd15_depth_fp16.yaml"}
    ],
    "4. Lineart": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_lineart_fp16.yaml"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15s2_lineart_anime_fp16.yaml"}
    ],
    "5. ip2p": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_ip2p_fp16.yaml"}
    ],
    "6. Shuffle": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11e_sd15_shuffle_fp16.yaml"}
    ],
    "7. Inpaint": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_inpaint_fp16.yaml"}
    ],
    "8. MLSD": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_mlsd_fp16.yaml"}
    ],
    "9. Normalbae": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_normalbae_fp16.yaml"}
    ],
    "10. Scribble": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_scribble_fp16.yaml"}
    ],
    "11. Seg": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_seg_fp16.yaml"}
    ],
    "12. Softedge": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11p_sd15_softedge_fp16.yaml"}
    ],
    "13. Tile": [
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile_fp16.safetensors"},
        {"url": "https://huggingface.co/ckpt/ControlNet-v1-1/raw/main/control_v11f1e_sd15_tile_fp16.yaml"}
    ]
}