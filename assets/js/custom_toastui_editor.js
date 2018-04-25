
var el = document.getElementById('id_contents')
var editor = tui.Editor.factory({
    el: document.getElementById('editSection'),
    initialEditType: 'markdown',
    initialValue : el.value,
    language:'ko-kr',
    previewStyle: 'vertical',
    height: 300,
    events: {
        change: function(e) {
            el.value = editor.preview.getHTML()
        }
    }
});