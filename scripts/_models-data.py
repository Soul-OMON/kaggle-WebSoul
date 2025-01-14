## MODEL

model_list = {
    "1. Stable Diffusion XL Base": {
        "url": "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors",
        "filename": "sd_xl_base_1.0.safetensors"
    },
    "2. Stable Diffusion v1.5": {
        "url": "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors",
        "filename": "v1-5-pruned.safetensors"
    },
    "3. Realistic Vision V5.1": {
        "url": "https://civitai.com/api/download/models/130072",
        "filename": "realisticVisionV51.safetensors"
    },
    "4. Counterfeit [Anime] [V3]": {
        "url": "https://civitai.com/api/download/models/57618",
        "filename": "CounterfeitV30.safetensors"
    },
    "5. DreamShaper XL": {
        "url": "https://civitai.com/api/download/models/126688",
        "filename": "dreamshaper_8.safetensors"
    },
    "6. RevAnimated": {
        "url": "https://civitai.com/api/download/models/46846",
        "filename": "revAnimated_v122.safetensors"
    },
    "7. Deliberate v3": {
        "url": "https://civitai.com/api/download/models/15236",
        "filename": "deliberate_v3.safetensors"
    },
    "8. AnythingV5": {
        "url": "https://civitai.com/api/download/models/30163",
        "filename": "anything-v5.safetensors"
    }
}

## VAE

vae_list = {
    "none": "Пропустить",
    "ALL": "Загрузить все",
    "1. SD-VAE": {
        "url": "https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors",
        "filename": "vae-ft-mse-840000-ema-pruned.safetensors"
    },
    "2. kl-f8-anime2": {
        "url": "https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt",
        "filename": "kl-f8-anime2.vae"
    },
    "3. Blessed2.vae": {
        "url": "https://civitai.com/api/download/models/30161",
        "filename": "blessed2.vae.pt"
    },
    "4. SD-XL.vae": {
        "url": "https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors",
        "filename": "sdxl_vae.safetensors"
    },
    "5. Counterfeit-XL.vae": {
        "url": "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_offset.safetensors",
        "filename": "sd_xl_offset.safetensors"
    }
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

clip_list = {
    "none": "Пропустить",
    "ALL": "Загрузить все",
    "1. CLIP-ViT-H-14": {
        "url": "https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K/resolve/main/model.safetensors",
        "filename": "clip-vit-h-14.safetensors"
    },
    "2. CLIP-ViT-bigG-14": {
        "url": "https://huggingface.co/laion/CLIP-ViT-bigG-14-laion2B-39B-b160k/resolve/main/model.safetensors",
        "filename": "clip-vit-bigg-14.safetensors"
    }
}