# Alfred Workflows

A collection of Alfred workflows that created by myself to make life easier.

## Installation

Download `*.alfredworkflow` and open in [Alfred3](https://www.alfredapp.com/).

Or clone the repo:`git clone https://github.com/BlackDragonF/AlfredWorkflows.git` and open `*.alfredworkflow` in Alfred3.

To use these workflows, you need to [buy the powerpack](https://www.alfredapp.com/powerpack/).

## Workflows

### Wireless

Connect to hotspots through Alfred. Download from [GitHub](https://github.com/BlackDragonF/AlfredWorkflows/raw/master/Wireless/Wireless.alfredworkflow).

#### Usage

1. `wireless <ssid>`--The WiFi you want to connect.
2. `<ssid> <password>[optional]`--if the WiFi has security, you should then extend password next to ssid in the following entry.

If something goes wrong, error log will be presented as notification.

### Meme

Generate animated-GIF mems using APIs provided by 'https://sorry.xuty.tk/sorry/' and copy the meme to clipboard. Download from [GitHub](https://github.com/BlackDragonF/AlfredWorkflows/raw/master/Meme/Meme.alfredworkflow).

#### Usage

`meme [template_name] sentence1|sentence2|…|sentence n`

Workflow will provide hints about all available templates and template's reference sentences. All gifs generated will be put into user's Downloads directory and then copied to clipboard.

#### Possible Bug

I wrote a tiny Objective-C command line program gif2clipboard to copy gif image to clipboard(by copying file-url to clipboard). 

It works fine on telegram but sometimes went wrong in macQQ and always fail in WeChat. I guess it depends on how different applications handle data from clipboard.

To provide more representations of gif image, issues/pull requests are welcomed :3

## License

MIT License (c) 码龙黑曜/CoSidian
