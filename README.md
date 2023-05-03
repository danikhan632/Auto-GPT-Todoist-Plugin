# Auto-GPT-Todoist


Auto-GPT-Todoist plugin transforms your task management experience, helping you stay organized, focused, and productive like never before.




![Alt Text](https://i.imgur.com/bYlbXjx.png)
### Plugin Installation Steps

for Linux, depending on distro
```
sudo apt-get install zip
apk add zip
sudo pacman -S zip
sudo yum install zip
```
Mac / Linux / WSL
```
cd plugins && git clone https://github.com/danikhan632/Auto-GPT-Todoist-Plugin.git && zip -r ./Auto-GPT-Todoist-Plugin.zip ./Auto-GPT-Todoist-Plugin && rm -rf ./Auto-GPT-Todoist-Plugin && cd .. && ./run.sh --install-plugin-deps

```
Windows, Powershell
```
cd plugins; git clone https://github.com/danikhan632/Auto-GPT-Todoist-Plugin.git; Compress-Archive -Path .\Auto-GPT-Todoist-Plugin -DestinationPath .\Auto-GPT-Todoist-Plugin.zip; Remove-Item -Recurse -Force .\Auto-GPT-Todoist-Plugin; cd ..
```



5. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ``` shell
   ALLOWLISTED_PLUGINS=AutoGPT-Todoist-Plugin
   TODOIST_TOKEN=Your_api_token
   ```

   If the plugin is not allowlisted, you will be warned before it's loaded.

