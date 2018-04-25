from django import forms


class SingleToastUIEditorWidget(forms.Textarea):
    template_name = 'widgets/toastui_editor_widget.html'

    class Media:
        css = {
            'all': [
                'bower_components/codemirror/lib/codemirror.css',
                'bower_components/highlightjs/styles/github.css',
                'bower_components/tui-editor/dist/tui-editor.css',
                'bower_components/tui-editor/dist/tui-editor-contents.css',
            ], }
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            'bower_components/tui-code-snippet/dist/tui-code-snippet.js',
            'bower_components/markdown-it/dist/markdown-it.js',
            'bower_components/to-mark/dist/to-mark.js',
            'bower_components/codemirror/lib/codemirror.js',
            'bower_components/highlightjs/highlight.pack.js',
            'bower_components/squire-rte/build/squire.js',
            'bower_components/tui-editor/dist/tui-editor-Editor.min.js',
            'js/custom_toastui_editor.js',
        ]

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['style'] = 'display:none'
        return attrs
