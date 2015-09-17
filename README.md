# Easy bootstrap featurette plugin

A Django-CMS plugin that allows easy creation of Bootstrap featurette elements.

## Description

This plugin for Django-CMS allows you to create Bootstrap featurette elements for your webpage. Three templates are included: one that renders images on the left and text on the right, one that renders images on the right and text on the left, and one that alternates between both templates.

Most portions of the featurette element are optional, allowing you to customize how your featurettes look. You can also optionally enter one or both desired dimensions (ie width and height) for your images, and the plugin will automatically resize them letting you focus on creating content instead of manually resizing images to optimize page load times. If you specify only image dimension then the plugin will resize each image proportionally in order to retain the original aspect ratio.

## Requirements

    Django-CMS
    Pillow
    Bootstrap

## Installation

Installation is simple and easy:

    Use pip to install

''' 
pip install djangocms_easy_featurette
'''

    Add the plugin to your INSTALLED_APPS in settings.py

''' 
INSTALLED_APPS = (
    ..., 
    djangocms_easy_featurette, 
    ...,
)
'''

Get Bootstrap if you don't have it already. It is not included with this plugin.

## License

This plugin is available under the MIT license.

## Contributing

If you find a bug or wish to add a new feature, please make a pull request to the development branch.
