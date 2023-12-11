// scripts.js

$(document).ready(function() {
    // Define additional options for each menu item
    var optionsForHome = [
        { text: 'Section 1', url: '{% url "dns" %}' },
        { text: 'Section 2', url: '{% url "distribution" %}' }
    ];

    // Add click event for menu items with submenu
    $('.has-submenu').click(function(e) {
        e.preventDefault();

        // Clear existing submenu options
        $(this).find('.submenu').empty();

        // Add new submenu options dynamically
        var options = $(this).is('.home') ? optionsForHome : [];
        options.forEach(function(option) {
            $(this).find('.submenu').append('<li><a href="' + option.url + '">' + option.text + '</a></li>');
        }.bind(this));

        // Show/hide submenu
        $(this).find('.submenu').toggle();
    });
});
