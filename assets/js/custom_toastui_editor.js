
var elContents = document.getElementById('id_contents')
var elConentsMarkdown = document.getElementById('id_contents_markdown')

var editor = tui.Editor.factory({
    el: document.getElementById('editSection'),
    initialEditType: 'markdown',
    initialValue : elConentsMarkdown.value,
    language:'ko-kr',
    previewStyle: 'vertical',
    height: 300,
    events: {
        change: function(e) {
            elContents.value = editor.preview.getHTML()
            elConentsMarkdown.value = editor.getValue()
        }
    }
});