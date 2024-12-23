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
SCR_PATH = Path(HOME / 'ANXETY')
SETTINGS_PATH = SCR_PATH / 'settings.json'
ENV_NAME = read_json(SETTINGS_PATH, 'ENVIRONMENT.env_name')

SCRIPTS = SCR_PATH / 'scripts'

CSS = SCR_PATH / 'CSS'
JS = SCR_PATH / 'JS'
widgets_css = CSS / 'main-widgets.css'
widgets_js = JS / 'main-widgets.js'

# ====================== WIDGETS =====================
def read_model_data(file_path, data_type):
    """
    Reads model, VAE, or ControlNet data from the specified file.

    The function loads data from a Python script and returns the corresponding list of model names based on the specified data type.

    Parameters:
    ----------
    file_path : str
        The path to the file containing model data in Python format.
    data_type : str
        The type of data to extract: "model", "vae", or "cnet".
    """
    local_vars = {}
    
    with open(file_path) as f:
        exec(f.read(), {}, local_vars)
    
    if data_type == "model":
        model_names = list(local_vars['model_list'].keys())   # Return model names
        return ['none'] + model_names
    elif data_type == "vae":
        vae_names = list(local_vars['vae_list'].keys())    # Return the VAE names
        return ['none', 'ALL'] + vae_names
    elif data_type == "cnet":
        cnet_names = list(local_vars['controlnet_list'].keys())   # Return ControlNet names
        return ['none', 'ALL'] + cnet_names

webui_selection = {
    'A1111': "--xformers --no-half-vae",
    'ReForge': "--xformers --cuda-stream --pin-shared-memory",
    'ComfyUI': "--dont-print-server --preview-method auto --use-pytorch-cross-attention",
    'Forge': "--opt-sdp-attention --cuda-stream --cuda-malloc --pin-shared-memory",  # Remove: --disable-xformers
    'SwarmUI': "--launch_mode none'"
}

# Initialize the WidgetFactory
factory = WidgetFactory()
HR = widgets.HTML('<hr>')

# --- MODEL ---
"""Create model selection widgets."""
model_header = factory.create_header('Model Selection')
model_options = model_options = read_model_data(f'{SCRIPTS}/_models-data.py', 'model')
model_widget = factory.create_dropdown(model_options, 'Model:', '4. Counterfeit [Anime] [V3] + INP')
model_num_widget = factory.create_text('Model Number:', '', 'Enter the model numbers for the download.')
inpainting_model_widget = factory.create_checkbox('Inpainting Models', False, class_names=['inpaint'])
XL_models_widget = factory.create_checkbox('SDXL', False, class_names=['sdxl'])

switch_model_widget = factory.create_hbox([inpainting_model_widget, XL_models_widget])

# --- VAE ---
"""Create VAE selection widgets."""
vae_header = factory.create_header('VAE Selection')
vae_options = read_model_data(f'{SCRIPTS}/_models-data.py', 'vae')
vae_widget = factory.create_dropdown(vae_options, 'Vae:', '3. Blessed2.vae')
vae_num_widget = factory.create_text('Vae Number:', '', 'Enter vae numbers for the download.')

# --- ADDITIONAL ---
"""Create additional configuration widgets."""
additional_header = factory.create_header('Additionally')
latest_webui_widget = factory.create_checkbox('Update WebUI', True)
latest_extensions_widget = factory.create_checkbox('Update Extensions', True)
check_custom_nodes_deps_widget = factory.create_checkbox('Check Custom-Nodes Dependencies', True)
change_webui_widget = factory.create_dropdown(list(webui_selection.keys()), 'WebUI:', 'A1111', layout={'width': 'auto'})
detailed_download_widget = factory.create_dropdown(['off', 'on'], 'Detailed Download:', 'off', layout={'width': 'auto'})
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
controlnet_num_widget = factory.create_text('ControlNet Number:', '', 'Enter the ControlNet model numbers for the download.')
commit_hash_widget = factory.create_text('Commit Hash:', '', 'Switching between branches or commits.')
civitai_token_widget = factory.create_text('CivitAI Token:', '', 'Enter your CivitAi API token.')
huggingface_token_widget = factory.create_text('HuggingFace Token:')

zrok_token_widget = factory.create_text('Zrok Token:')
zrok_button = factory.create_html('<a href="https://colab.research.google.com/drive/1d2sjWDJi_GYBUavrHSuQyHTDuLy36WpU" target="_blank">Register Zrok Token</a>', class_names=["button", "button_ngrok"])
zrok_widget = factory.create_hbox([zrok_token_widget, zrok_button])

commandline_arguments_widget = factory.create_text('Arguments:', webui_selection['A1111'])

additional_widget_list = [
    additional_header, choose_changes_widget, HR, controlnet_widget, controlnet_num_widget,
    commit_hash_widget,
    civitai_token_widget, huggingface_token_widget, zrok_widget, HR, commandline_arguments_widget
]

# --- CUSTOM DOWNLOAD ---
"""Create Custom-Download Selection widgets."""
custom_download_header_popup = factory.create_html('''
<div class="header" style="cursor: pointer;" onclick="toggleContainer()">Custom Download</div>
<div class="info" id="info_dl">INFO</div>
<div class="popup">
    Separate multiple URLs with a comma/space. For a <span class="file_name">custom name</span> file/extension, specify it with <span class="braces">[]</span> after the URL without spaces.
    <span style="color: #ff9999">For files, be sure to specify</span> - <span class="extension">Filename Extension.</span>
    <div class="sample">
        <span class="sample_label">Example for File:</span>
        https://civitai.com/api/download/models/229782<span class="braces">[</span><span class="file_name">Detailer</span><span class="extension">.safetensors</span><span class="braces">]</span>
        <br>
        <span class="sample_label">Example for Extension:</span>
        https://github.com/hako-mikan/sd-webui-regional-prompter<span class="braces">[</span><span class="file_name">Regional-Prompter</span><span class="braces">]</span>
    </div>
</div>
''')

Model_url_widget = factory.create_text('Model:')
Vae_url_widget = factory.create_text('Vae:')
LoRA_url_widget = factory.create_text('LoRa:')
Embedding_url_widget = factory.create_text('Embedding:')
Extensions_url_widget = factory.create_text('Extensions:')
custom_file_urls_widget = factory.create_text('File (txt):')

# --- Save Button ---
"""Create button widgets."""
save_button = factory.create_button('Save', class_names=["button", "button_save"])

# ================ DISPLAY / SETTINGS ================

factory.load_css(widgets_css)   # load CSS (widgets)
factory.load_js(widgets_js)     # load JS (widgets)

# Display sections
model_widgets = [model_header, model_widget, model_num_widget, switch_model_widget]
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
    factory.close(list(WIDGET_LIST.children), class_names=['hide'], delay=0.5)

load_settings()
save_button.on_click(save_data)