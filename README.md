# Convert-SVG-embeded-images-to-png
Convert SVG files to png and replace the code with a called to the image file in Markdown files. This project is a fork of [convert-svg-to-png](https://github.com/joseaeltala/convert-svg-to-png) that convert svg code in a Markdown file, instead of embeded images itself.

# Objectives
Email clients (like Gmail) not render svg files, so if we want to send Markdown file with svg images, we have to convert before.

# Inputs
| NAME | VALUE | DEFAULT | DESCRIPTION |
| ---- | ----- | ------- | ----------- |
| file | string | README.md | The file from which the SVG code will be collected and in which the code will be replaced by a call to the generated PNG|
| path | string | Images/ | The path where the PNG file will go |
| name | string | Draw | The filename format to save the PNG file |

# Example Workflow file
    on: push
    jobs:
      Makefiles:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v1
          - name: convert-svg-to-png
            uses: oriolpiera/convert-svg-to-png/@master
            with:
              file: "README.md"
              path: "Images/png" # Existing folders
              name: "converted-svg-file"
          - name: Commit files
            run: |
              git config user.name github-actions
              git config user.email github-actions@github.com
              git commit -m "SVG code converted to png" -a
          - name: Push changes
            uses: ad-m/github-push-action@master
            with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              branch: ${{ github.ref }}
