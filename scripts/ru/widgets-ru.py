# ~ widgets.py | by ANXETY ~

from json_utils import read_json, save_json, update_json  # JSON (main)
from json_utils import key_or_value_exists, delete_key    # JSON (other)
from widget_factory import WidgetFactory                  # WIDGETS
from webui_utils import update_current_webui              # WEBUI

import ipywidgets as widgets
from pathlib import Path
import os

# Constants
HOME = Path.home()
SCR_PATH = Path(HOME / 'SOUL')
SETTINGS_PATH = SCR_PATH / 'settings.json'
ENV_NAME = read_json(SETTINGS_PATH, 'ENVIRONMENT.env_name')

SCRIPTS = SCR_PATH / 'scripts'

CSS = SCR_PATH / 'CSS'
JS = SCR_PATH / 'JS'
widgets_css = CSS / 'main-widgets.css'
widgets_js = JS / 'main-widgets.js'

# ====================== WIDGETS =====================
def read_model_data(file_path, data_type):
    """Read model data from file."""
    local_vars = {}
    
    print(f"Reading {data_type} data from {file_path}")  # Отладочный вывод
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        exec(content, {}, local_vars)
    
    # Проверяем, какие данные есть в файле
    print(f"Available keys in local_vars: {list(local_vars.keys())}")  # Отладочный вывод
    
    data_key = f'{data_type.upper()}_DATA'
    data = local_vars.get(data_key, {})
    
    print(f"Data for {data_key}: {list(data.keys())}")  # Отладочный вывод
    
    if not data:
        print(f"No data found for {data_key}")  # Отладочный вывод
        return ['none']
    
    if data_type == 'model':
        return list(data.keys())
    elif data_type in ['vae', 'clip', 'controlnet']:
        base_options = ['none', 'ALL']
        additional_options = [k for k in data.keys() if k not in base_options]
        return base_options + additional_options
    else:
        return list(data.keys())

webui_selection = {
    'A1111': "--xformers --no-half-vae",
    'ReForge': "--xformers --cuda-stream --pin-shared-memory",
    'ComfyUI': "--dont-print-server --preview-method auto --use-pytorch-cross-attention",
    'Forge': "--opt-sdp-attention --cuda-stream --cuda-malloc --pin-shared-memory"  # Remove: --disable-xformers 
}

# Initialize the WidgetFactory
factory = WidgetFactory()
HR = widgets.HTML('<hr>')

# --- MODEL ---
"""Create model selection widgets."""
model_header = factory.create_header('Выбор Модели')
model_options = read_model_data(f'{SCRIPTS}/_models-data.py', 'model')
print(f"Model options: {model_options}")  # Отладочный вывод
model_widget = factory.create_dropdown(
    options=model_options,
    description='Модель:',
    value=model_options[0] if model_options else 'none'
)
model_num_widget = factory.create_text('Номер Модели:', '', 'Введите номера моделей для скачивания.')
inpainting_model_widget = factory.create_checkbox('Inpainting Модели', False, class_names=['inpaint'])
XL_models_widget = factory.create_checkbox('SDXL', False, class_names=['sdxl'])

switch_model_widget = factory.create_hbox([inpainting_model_widget, XL_models_widget])

# --- VAE ---
"""Create VAE selection widgets."""
vae_header = factory.create_header('Выбор VAE')
vae_options = read_model_data(f'{SCRIPTS}/_models-data.py', 'vae')
print(f"VAE options: {vae_options}")  # Отладочный вывод
vae_widget = factory.create_dropdown(
    options=vae_options,
    description='Vae:',
    value='none'
)
vae_num_widget = factory.create_text('Номер Vae:', '', 'Введите номера vae для скачивания.')

# --- CLIP ---
clip_header = factory.create_header('Выбор CLIP')
clip_options = read_model_data(f'{SCRIPTS}/_models-data.py', 'clip')
clip_widget = factory.create_dropdown(
    options=clip_options,
    description='CLIP:',
    value='none'  # Для CLIP тоже начинаем с 'none'
)
clip_num_widget = factory.create_text(
    description='Номер CLIP:',
    value='',
    placeholder='Введите номера CLIP для скачивания.'
)

# --- ADDITIONAL ---
"""Create additional configuration widgets."""
additional_header = factory.create_header('Дополнительно')
latest_webui_widget = factory.create_checkbox('Обновить WebUI', True)
latest_extensions_widget = factory.create_checkbox('Обновить Расширения', True)
check_custom_nodes_deps_widget = factory.create_checkbox('Чекать зависимости Custom-Nodes', True)
change_webui_widget = factory.create_dropdown(list(webui_selection.keys()), 'WebUI:', 'A1111')
detailed_download_widget = factory.create_dropdown(['off', 'on'], 'Подробная Загрузка:', 'off', layout={'width': 'auto'})
choose_changes_widget = factory.create_hbox(
    [
        latest_webui_widget,
        latest_extensions_widget,
        check_custom_nodes_deps_widget,   # Only ComfyUI
        change_webui_widget,
        detailed_download_widget
    ],
    layout={'justify_content': 'space-between'}
)

controlnet_options = read_model_data(f'{SCRIPTS}/_models-data.py', 'cnet')
controlnet_widget = factory.create_dropdown(controlnet_options, 'ControlNet:', 'none')
controlnet_num_widget = factory.create_text('Номер ControlNet:', '', 'Введите номера моделей ControlNet для скачивания.')
commit_hash_widget = factory.create_text('Commit Hash:', '', 'Переключение между ветвями или коммитами.')
civitai_token_widget = factory.create_text('Токен CivitAI:', '', 'Введите свой API-токен CivitAi.')
huggingface_token_widget = factory.create_text('Токен HuggingFace:')

ngrok_token_widget = factory.create_text('Токен Ngrok:')
ngrok_button = factory.create_html('<a href="https://dashboard.ngrok.com/get-started/your-authtoken" target="_blank">Получить Ngrok Токен</a>', class_names=["button", "button_zrok"])
ngrok_widget = factory.create_hbox([ngrok_token_widget, ngrok_button])

zrok_token_widget = factory.create_text('Токен Zrok:')
zrok_button = factory.create_html('<a href="https://colab.research.google.com/drive/1d2sjWDJi_GYBUavrHSuQyHTDuLy36WpU" target="_blank">Зарегать Zrok Токен</a>', class_names=["button", "button_zrok"])
zrok_widget = factory.create_hbox([zrok_token_widget, zrok_button])

commandline_arguments_widget = factory.create_text('Аргументы:', webui_selection['A1111'])

additional_widget_list = [
    additional_header,
    choose_changes_widget,
    HR,
    controlnet_widget, controlnet_num_widget,
    commit_hash_widget,
    civitai_token_widget, huggingface_token_widget, zrok_widget, ngrok_widget,
    HR,
    commandline_arguments_widget
]
# if ENV_NAME == "Google Colab": # remove ngrok from colab
#     additional_widget_list.remove(ngrok_widget)

# --- CUSTOM DOWNLOAD ---
"""Create custom download widgets."""
custom_download_header = factory.create_header('Пользовательская Загрузка')
custom_download_header_popup = factory.create_header('🔗 Пользовательские ссылки')

# URL widgets
Model_url_widget = factory.create_text('Model URL:', '', 'Введите прямую ссылку на модель')
Vae_url_widget = factory.create_text('VAE URL:', '', 'Введите прямую ссылку на VAE')
LoRA_url_widget = factory.create_text('LoRA URL:', '', 'Введите прямую ссылку на LoRA')
Embedding_url_widget = factory.create_text('Embedding URL:', '', 'Введите прямую ссылку на Embedding')
Extensions_url_widget = factory.create_text('Extensions URL:', '', 'Введите прямую ссылку на расширение')
ADetailer_url_widget = factory.create_text('ADetailer URL:', '', 'Введите прямую ссылку на ADetailer')

# Custom file URLs
custom_file_urls_widget = factory.create_text(
    'Custom URLs:',
    '',
    'Введите прямые ссылки, разделенные запятыми (http://..., http://...)'
)

# Группируем виджеты
custom_download_widgets = [
    custom_download_header_popup,
    Model_url_widget,
    Vae_url_widget,
    LoRA_url_widget,
    Embedding_url_widget,
    Extensions_url_widget,
    ADetailer_url_widget,
    custom_file_urls_widget
]

custom_download_box = factory.create_vbox([custom_download_header] + custom_download_widgets)

# --- SAVE BUTTON ---
"""Create save button."""
save_button = factory.create_button(
    'Сохранить',
    'success',
    icon='save'
)

# Объединяем все в один вертикальный контейнер
WIDGET_LIST = factory.create_vbox([
    model_box,
    vae_box,
    clip_box,
    additional_box,
    custom_download_box,
    save_button
], layouts=[{'width': '1080px'}]*6)

# ================ DISPLAY / SETTINGS ================

factory.load_css(widgets_css)   # load CSS (widgets)
factory.load_js(widgets_js)     # load JS (widgets)

# Display sections
model_widgets = [model_header, model_widget, model_num_widget, switch_model_widget]
vae_widgets = [vae_header, vae_widget, vae_num_widget]
clip_widgets = [clip_header, clip_widget, clip_num_widget]
additional_widgets = additional_widget_list
custom_download_widgets = [
    custom_download_header_popup,
    Model_url_widget,
    Vae_url_widget,
    LoRA_url_widget,
    Embedding_url_widget,
    Extensions_url_widget,
    ADetailer_url_widget,
    custom_file_urls_widget
]

# Create Boxes
model_box = factory.create_vbox(model_widgets, class_names=["container"])
vae_box = factory.create_vbox(vae_widgets, class_names=["container"])
clip_box = factory.create_vbox(clip_widgets, class_names=["container"])
additional_box = factory.create_vbox(additional_widgets, class_names=["container"])
custom_download_box = factory.create_vbox(custom_download_widgets, class_names=["container", "container_cdl"])

# ================ CALLBACK FUNCTION ================
# Callback functions for updating widgets
def update_change_webui(change, widget):
    selected_webui = change['new']
    commandline_arguments = webui_selection.get(selected_webui, "")
    commandline_arguments_widget.value = commandline_arguments
    
    if selected_webui == 'ComfyUI':
        latest_extensions_widget.layout.display = 'none'
        latest_extensions_widget.value = False
        check_custom_nodes_deps_widget.layout.display = 'inline-block'
        Extensions_url_widget.description = 'Custom Nodes:'
    else:
        latest_extensions_widget.layout.display = 'inline-block'
        latest_extensions_widget.value = True
        check_custom_nodes_deps_widget.layout.display = 'none'
        Extensions_url_widget.description = 'Extensions:'

# Initialize visibility of the check dependencies widget
check_custom_nodes_deps_widget.layout.display = 'none'  # Initially hidden

def update_XL_options(change, widget):
    selected = change['new']

    default_model_values = {
        True: ('1. Nova [Anime] [V7] [XL]', '1. sdxl.vae', 'none'),   # For XL models
        False: ('4. Counterfeit [Anime] [V3] + INP', '3. Blessed2.vae', 'none')   # For 1.5 models
    }

    # GET DATA MODELs | VAES| CNETs
    data_file = '_xl-models-data.py' if selected else '_models-data.py'
    model_widget.options = read_model_data(f'{SCRIPTS}/{data_file}', 'model')
    vae_widget.options = read_model_data(f'{SCRIPTS}/{data_file}', 'vae')
    controlnet_widget.options = read_model_data(f'{SCRIPTS}/{data_file}', 'cnet')

    # Set default values from the dictionary
    model_widget.value, vae_widget.value, controlnet_widget.value = default_model_values[selected]
    
# Connecting widgets
factory.connect_widgets([(change_webui_widget, 'value')], [update_change_webui])
factory.connect_widgets([(XL_models_widget, 'value')], [update_XL_options])

## ============ Load / Save - Settings V3 ============

SETTINGS_KEYS = [
    'XL_models', 'model', 'model_num', 'inpainting_model',
    'vae', 'vae_num',
    'clip', 'clip_num',  # Добавляем CLIP
    'latest_webui', 'latest_extensions', 'check_custom_nodes_deps',
    'change_webui', 'detailed_download',
    'controlnet', 'controlnet_num', 'commit_hash',
    'civitai_token', 'huggingface_token', 'zrok_token', 'ngrok_token',
    'commandline_arguments',
    'Model_url', 'Vae_url', 'LoRA_url', 'Embedding_url', 'Extensions_url',
    'ADetailer_url', 'custom_file_urls'
]

def save_settings():
    """Save widget values to settings."""
    widgets_values = {key: globals()[f"{key}_widget"].value for key in SETTINGS_KEYS}
    save_json(SETTINGS_PATH, "WIDGETS", widgets_values)

    update_current_webui(change_webui_widget.value)  # Upadte Selected WebUI in setting.json

def load_settings():
    """Load widget values from settings."""
    if key_or_value_exists(SETTINGS_PATH, 'WIDGETS'):
        widget_data = read_json(SETTINGS_PATH, 'WIDGETS')
        for key in SETTINGS_KEYS:
            if key in widget_data:
                globals()[f"{key}_widget"].value = widget_data.get(key, "")

def save_data(button):
    """Handle save button click."""
    save_settings()
    factory.close(list(WIDGET_LIST.children), class_names=['hide'], delay=0.8)

load_settings()
save_button.on_click(save_data)