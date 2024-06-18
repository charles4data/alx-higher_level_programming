document.addEventListener('DOMContentLoaded', function() {
    $(function() {
        let itemCounter = 1;

        // Adding item
        $('#add_item').click(function() {
            $('UL.my_list').append(`<li>Item ${itemCounter}</li>`);
            itemCounter++;
        });

        // Removing item
        $('#remove_item').click(function() {
            $('UL.my_list li:last').remove();
            itemCounter = Math.max(1, itemCounter - 1);
        });

        // Clearing list
        $('#clear_list').click(function() {
            $('UL.my_list').empty();
            itemCounter = 1;
        });
    });
});
