<%@ Language=VBScript %>

<script language="JScript" runat="server" src="./identical/identical_data.js"></script>
<script language="JScript" runat="server">
var search_id = 32992;

function get_filenames_for_model_id(id) {
    var result, i, key;
    result = [];
    for (key in hash_by_file) {
        i = key.indexOf('/');
        if (key.substr(0, i) == id) {
            result.push(key.substr(i));
        }
    }
    return result;
}

files = get_filenames_for_model_id(search_id);

result = '';
var i;
for (i = 0; i < files.length; i++) {
    result += files[i] + '    ';
}
hash_by_file = result;
</script>

hash_by_file = <% =hash_by_file %>

