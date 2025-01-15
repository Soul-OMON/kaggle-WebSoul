## MODEL

model_list = {
    "1. Flux1-dev-bnb-nf4 (Включены VAE)": [
        {"url": "https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4/resolve/main/flux1-dev-bnb-nf4-v2.safetensors", "name": "flux1-dev-bnb-nf4-v2.safetensors"}
    ],
    "2. Flux1-dev-fp8 (Требует все VAE)": [
        {"url": "https://huggingface.co/lllyasviel/flux1_dev/resolve/main/flux1-dev-fp8.safetensors", "name": "flux1-dev-fp8.safetensors"}
    ]

}

## VAE

vae_list = {
        "1. t5xxl fp8": [
        {"url": "https://huggingface.co/lllyasviel/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors", "name": "t5xxl_fp8_e4m3fn.safetensors"}
    ],
       "2. ae": [
        {"url": "https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/ae.safetensors", "name": "ae.safetensors"}
    ],
       "3. clip_l": [
        {"url": "https://huggingface.co/lllyasviel/flux_text_encoders/resolve/main/clip_l.safetensors", "name": "clip_l.safetensors"}
    ],
       "4. t5xxl_fp16": [
        {"url": "https://huggingface.co/lllyasviel/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors", "name": "t5xxl_fp16.safetensors"}
    ]
}

## CONTROLNET

controlnet_list = {
    "1. Kohya Controllite XL Blur": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_blur.safetensors"},
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_blur_anime.safetensors"}
    ],
    "2.Kohya Controllite XL Canny": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_canny.safetensors"},
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_canny_anime.safetensors"}
    ],
    "3. Kohya Controllite XL Depth": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_depth.safetensors"},
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_depth_anime.safetensors"}
    ],
    "4. Kohya Controllite XL Openpose Anime": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_openpose_anime.safetensors"},
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_openpose_anime_v2.safetensors"}
    ],
    "5. Kohya Controllite XL Scribble Anime": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/kohya_controllllite_xl_scribble_anime.safetensors"}
    ],
    "6. T2I Adapter XL Canny": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_canny.safetensors"}
    ],
    "7. T2I Adapter XL Openpose": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_openpose.safetensors"}
    ],
    "8. T2I Adapter XL Sketch": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_xl_sketch.safetensors"}
    ],
    "9. T2I Adapter Diffusers XL Canny": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_canny.safetensors"}
    ],
    "10. T2I Adapter Diffusers XL Depth Midas": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_depth_midas.safetensors"}
    ],
    "11. T2I Adapter Diffusers XL Depth Zoe": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_depth_zoe.safetensors"}
    ],
    "12. T2I Adapter Diffusers XL Lineart": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_lineart.safetensors"}
    ],
    "13. T2I Adapter Diffusers XL Openpose": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_openpose.safetensors"}
    ],
    "14. T2I Adapter Diffusers XL Sketch": [
        {"url": "https://huggingface.co/lllyasviel/sd_control_collection/resolve/main/t2i-adapter_diffusers_xl_sketch.safetensors"}
    ]
}