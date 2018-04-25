var elContents = document.getElementById('id_contents')
var elConentsMarkdown = document.getElementById('id_contents_markdown')

var editor = $('#editSection').tuiEditor({
    initialEditType: 'markdown',
    previewStyle: 'vertical',
    initialValue: elConentsMarkdown.value,
    height: 'auto',
    events: {
        change: function(e) {
            var markdown = editor.data('tuiEditor').getMarkdown();
            elContents.value = editor.data('tuiEditor').convertor.toHTML(markdown)
            elConentsMarkdown.value = markdown;
        }
    }
});