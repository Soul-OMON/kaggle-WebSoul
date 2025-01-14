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

    try:
        with open(file_path) as f:
            exec(f.read(), {}, local_vars)
        
        data = local_vars.get(f'{data_type.upper()}_DATA', {})
        
        # Для VAE добавляем специальные опции
        if data_type == 'vae':
            if isinstance(data, dict):
                return ['none', 'ALL'] + list(data.keys())
            return ['none', 'ALL'] + list(data)
            
        return data
    except Exception as e:
        print(f"Error reading model data: {e}")
        return ['none']  # Возвращаем минимальный список с 'none'

webui_selection = {
    'A1111': "--xformers --no-half-vae",
    'ReForge': "--xformers --cuda-stream --pin-shared-memory",
    'ComfyUI': "--dont-print-server --preview-method auto --use-pytorch-cross-attention",
    'Forge': "--opt-sdp-attention --cuda-stream --cuda-malloc --pin-shared-memory"  # Remove: --disable-xformers 
}

# Initialize the WidgetFactory
factory = WidgetFactory()
HR = widgets.HTML('<hr>')

# Создание категорий моделей
model_categories = {
    'Общие': ['Stable Diffusion XL Base', 'Stable Diffusion v1.5'],
    'Аниме': ['AnythingV5', 'CounterfeitV30'],
    'Реализм': ['Realistic Vision V5.1', 'PhotonV1'],
    'Стилизация': ['Deliberate v3', 'RevAnimated v122']
}

# Создание виджета выбора категории
categories = list(model_categories.keys())
category_widget = factory.create_dropdown(
    options=categories,
    description='Категория модели:',
    value=categories[0]
)

# Создание виджета выбора модели
models = model_categories['Общие']  # Начальные модели из категории "Общие"
model_widget = factory.create_dropdown(
    options=models,
    description='Модель:',
    value=models[0]
)

# Обработчик изменения категории
def on_category_change(change):
    model_widget.options = model_categories[change['new']]
    model_widget.value = model_categories[change['new']][0]

category_widget.observe(on_category_change, names='value')

# --- VAE ---
"""Create VAE selection widgets."""
vae_header = factory.create_header('Выбор VAE')
vae_options = read_model_data(f'{SCRIPTS}/_models-data.py', 'vae')

# Добавим отладочный вывод
print("Available VAE options:", vae_options)

# Создаем список опций с гарантированным значением 'none'
if isinstance(vae_options, dict):
    vae_list = list(vae_options.keys())
else:
    vae_list = list(vae_options)

if 'none' not in vae_list:
    vae_list.insert(0, 'none')

vae_widget = factory.create_dropdown(
    options=vae_list,
    description='Vae:',
    value=vae_list[0]  # Используем первый элемент списка как значение по умолчанию
)

vae_num_widget = factory.create_text(
    description='Номер Vae:', 
    value='', 
    placeholder='Введите номера vae для скачивания.'
)

# --- ADDITIONAL ---
"""Create additional configuration widgets."""
additional_header = factory.create_header('Дополнительно')
latest_webui_widget = factory.create_checkbox('Обновить WebUI', True)
latest_extensions_widget = factory.create_checkbox('Обновить Расширения', True)
check_custom_nodes_deps_widget = factory.create_checkbox('Чекать зависимости Custom-Nodes', True)
change_webui_widget = factory.create_dropdown(list(webui_selection.keys()), 'WebUI:', 'A1111', layout={'width': 'auto'})
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

zrok_token_widget = factory.create_text('Токен Zrok:')
zrok_button = factory.create_html('<a href="https://colab.research.google.com/drive/1d2sjWDJi_GYBUavrHSuQyHTDuLy36WpU" target="_blank">Зарегать Zrok Токен</a>', class_names=["button", "button_zrok"])
zrok_widget = factory.create_hbox([zrok_token_widget, zrok_button])

commandline_arguments_widget = factory.create_text('Аргументы:', webui_selection['A1111'])

additional_widget_list = [
    additional_header, choose_changes_widget, HR, controlnet_widget, controlnet_num_widget,
    commit_hash_widget,
    civitai_token_widget, huggingface_token_widget, zrok_widget, HR, commandline_arguments_widget
]

# --- CUSTOM DOWNLOAD ---
"""Create Custom-Download Selection widgets."""
custom_download_header_popup = factory.create_html('''
<div class="header" style="cursor: pointer;" onclick="toggleContainer()">Кастомная Загрузка</div>
<div class="info" id="info_dl">INFO</div>
<div class="popup">
    Разделите несколько URL-адресов запятой/пробелом. Для <span class="file_name">пользовательского имени</span> файла/расширения укажите его через <span class="braces">[]</span> после URL без пробелов.
    <span class="required">Для файлов обязательно укажите</span> - <span class="extension">Расширение Файла.</span>
    <div class="sample">
        <span class="sample_label">Пример для Файла:</span>
        https://civitai.com/api/download/models/229782<span class="braces">[</span><span class="file_name">Detailer</span><span class="extension">.safetensors</span><span class="braces">]</span>
        <br>
        <span class="sample_label">Пример для Расширения:</span>
        https://github.com/hako-mikan/sd-webui-regional-prompter<span class="braces">[</span><span class="file_name">Regional-Prompter</span><span class="braces">]</span>
    </div>
</div>
''')

Model_url_widget = factory.create_text('Model:')
Vae_url_widget = factory.create_text('Vae:')
LoRA_url_widget = factory.create_text('LoRa:')
Embedding_url_widget = factory.create_text('Embedding:')
Extensions_url_widget = factory.create_text('Extensions:')
custom_file_urls_widget = factory.create_text('Файл (txt):')

# --- Save Button ---
"""Create button widgets."""
save_button = factory.create_button('Сохранить', class_names=["button", "button_save"])

# ================ DISPLAY / SETTINGS ================

factory.load_css(widgets_css)   # load CSS (widgets)
factory.load_js(widgets_js)     # load JS (widgets)

# Display sections
model_widgets = [category_widget, model_widget]
vae_widgets = [vae_header, vae_widget, vae_num_widget]
additional_widgets = additional_widget_list
custom_download_widgets = [
    custom_download_header_popup,
    Model_url_widget,
    Vae_url_widget,
    LoRA_url_widget,
    Embedding_url_widget,
    Extensions_url_widget,
    custom_file_urls_widget
]

# Create Boxes
model_box = factory.create_vbox(model_widgets, class_names=["container"])
vae_box = factory.create_vbox(vae_widgets, class_names=["container"])
additional_box = factory.create_vbox(additional_widgets, class_names=["container"])
custom_download_box = factory.create_vbox(custom_download_widgets, class_names=["container", "container_cdl"])

WIDGET_LIST = factory.create_vbox([model_box, vae_box, additional_box, custom_download_box, save_button],
                                  layouts=[{'width': '1080px'}]*4)    # style for the first four elements
factory.display(WIDGET_LIST)

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
      'XL_models', 'model', 'model_num', 'inpainting_model', 'vae', 'vae_num',
      'latest_webui', 'latest_extensions', 'check_custom_nodes_deps', 'change_webui', 'detailed_download',
      'controlnet', 'controlnet_num', 'commit_hash',
      'civitai_token', 'huggingface_token', 'zrok_token', 'commandline_arguments',
      'Model_url', 'Vae_url', 'LoRA_url', 'Embedding_url', 'Extensions_url', 'custom_file_urls'
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