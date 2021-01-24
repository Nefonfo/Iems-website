# Generated by Django 3.1.5 on 2021-01-24 00:43

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210123_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('hero_header', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=30, min_length=2)), ('dynamic_text', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(help_text='Titulo Dinámico', max_length=30, min_length=1))), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=70, min_length=10)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=70, min_length=3)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('skills', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10)), ('skills', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='Tecnología', max_length=20, min_length=1)), ('percentage', wagtail.core.blocks.FloatBlock(help_text='Porcentaje', max_value=100, min_value=0)), ('image', wagtail.images.blocks.ImageChooserBlock())])))])), ('features', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10)), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('fa-500px', '500px'), ('fa-address-book', 'address-book'), ('fa-address-book-o', 'address-book-o'), ('fa-address-card', 'address-card'), ('fa-address-card-o', 'address-card-o'), ('fa-adjust', 'adjust'), ('fa-adn', 'adn'), ('fa-align-center', 'align-center'), ('fa-align-justify', 'align-justify'), ('fa-align-left', 'align-left'), ('fa-align-right', 'align-right'), ('fa-amazon', 'amazon'), ('fa-ambulance', 'ambulance'), ('fa-american-sign-language-interpreting', 'american-sign-language-interpreting'), ('fa-anchor', 'anchor'), ('fa-android', 'android'), ('fa-angellist', 'angellist'), ('fa-angle-double-down', 'angle-double-down'), ('fa-angle-double-left', 'angle-double-left'), ('fa-angle-double-right', 'angle-double-right'), ('fa-angle-double-up', 'angle-double-up'), ('fa-angle-down', 'angle-down'), ('fa-angle-left', 'angle-left'), ('fa-angle-right', 'angle-right'), ('fa-angle-up', 'angle-up'), ('fa-apple', 'apple'), ('fa-archive', 'archive'), ('fa-area-chart', 'area-chart'), ('fa-arrow-circle-down', 'arrow-circle-down'), ('fa-arrow-circle-left', 'arrow-circle-left'), ('fa-arrow-circle-o-down', 'arrow-circle-o-down'), ('fa-arrow-circle-o-left', 'arrow-circle-o-left'), ('fa-arrow-circle-o-right', 'arrow-circle-o-right'), ('fa-arrow-circle-o-up', 'arrow-circle-o-up'), ('fa-arrow-circle-right', 'arrow-circle-right'), ('fa-arrow-circle-up', 'arrow-circle-up'), ('fa-arrow-down', 'arrow-down'), ('fa-arrow-left', 'arrow-left'), ('fa-arrow-right', 'arrow-right'), ('fa-arrow-up', 'arrow-up'), ('fa-arrows', 'arrows'), ('fa-arrows-alt', 'arrows-alt'), ('fa-arrows-h', 'arrows-h'), ('fa-arrows-v', 'arrows-v'), ('fa-asl-interpreting', 'asl-interpreting'), ('fa-assistive-listening-systems', 'assistive-listening-systems'), ('fa-asterisk', 'asterisk'), ('fa-at', 'at'), ('fa-audio-description', 'audio-description'), ('fa-automobile', 'automobile'), ('fa-backward', 'backward'), ('fa-balance-scale', 'balance-scale'), ('fa-ban', 'ban'), ('fa-bandcamp', 'bandcamp'), ('fa-bank', 'bank'), ('fa-bar-chart', 'bar-chart'), ('fa-bar-chart-o', 'bar-chart-o'), ('fa-barcode', 'barcode'), ('fa-bars', 'bars'), ('fa-bath', 'bath'), ('fa-bathtub', 'bathtub'), ('fa-battery', 'battery'), ('fa-battery-0', 'battery-0'), ('fa-battery-1', 'battery-1'), ('fa-battery-2', 'battery-2'), ('fa-battery-3', 'battery-3'), ('fa-battery-4', 'battery-4'), ('fa-battery-empty', 'battery-empty'), ('fa-battery-full', 'battery-full'), ('fa-battery-half', 'battery-half'), ('fa-battery-quarter', 'battery-quarter'), ('fa-battery-three-quarters', 'battery-three-quarters'), ('fa-bed', 'bed'), ('fa-beer', 'beer'), ('fa-behance', 'behance'), ('fa-behance-square', 'behance-square'), ('fa-bell', 'bell'), ('fa-bell-o', 'bell-o'), ('fa-bell-slash', 'bell-slash'), ('fa-bell-slash-o', 'bell-slash-o'), ('fa-bicycle', 'bicycle'), ('fa-binoculars', 'binoculars'), ('fa-birthday-cake', 'birthday-cake'), ('fa-bitbucket', 'bitbucket'), ('fa-bitbucket-square', 'bitbucket-square'), ('fa-bitcoin', 'bitcoin'), ('fa-black-tie', 'black-tie'), ('fa-blind', 'blind'), ('fa-bluetooth', 'bluetooth'), ('fa-bluetooth-b', 'bluetooth-b'), ('fa-bold', 'bold'), ('fa-bolt', 'bolt'), ('fa-bomb', 'bomb'), ('fa-book', 'book'), ('fa-bookmark', 'bookmark'), ('fa-bookmark-o', 'bookmark-o'), ('fa-braille', 'braille'), ('fa-briefcase', 'briefcase'), ('fa-btc', 'btc'), ('fa-bug', 'bug'), ('fa-building', 'building'), ('fa-building-o', 'building-o'), ('fa-bullhorn', 'bullhorn'), ('fa-bullseye', 'bullseye'), ('fa-bus', 'bus'), ('fa-buysellads', 'buysellads'), ('fa-cab', 'cab'), ('fa-calculator', 'calculator'), ('fa-calendar', 'calendar'), ('fa-calendar-check-o', 'calendar-check-o'), ('fa-calendar-minus-o', 'calendar-minus-o'), ('fa-calendar-o', 'calendar-o'), ('fa-calendar-plus-o', 'calendar-plus-o'), ('fa-calendar-times-o', 'calendar-times-o'), ('fa-camera', 'camera'), ('fa-camera-retro', 'camera-retro'), ('fa-car', 'car'), ('fa-caret-down', 'caret-down'), ('fa-caret-left', 'caret-left'), ('fa-caret-right', 'caret-right'), ('fa-caret-square-o-down', 'caret-square-o-down'), ('fa-caret-square-o-left', 'caret-square-o-left'), ('fa-caret-square-o-right', 'caret-square-o-right'), ('fa-caret-square-o-up', 'caret-square-o-up'), ('fa-caret-up', 'caret-up'), ('fa-cart-arrow-down', 'cart-arrow-down'), ('fa-cart-plus', 'cart-plus'), ('fa-cc', 'cc'), ('fa-cc-amex', 'cc-amex'), ('fa-cc-diners-club', 'cc-diners-club'), ('fa-cc-discover', 'cc-discover'), ('fa-cc-jcb', 'cc-jcb'), ('fa-cc-mastercard', 'cc-mastercard'), ('fa-cc-paypal', 'cc-paypal'), ('fa-cc-stripe', 'cc-stripe'), ('fa-cc-visa', 'cc-visa'), ('fa-certificate', 'certificate'), ('fa-chain', 'chain'), ('fa-chain-broken', 'chain-broken'), ('fa-check', 'check'), ('fa-check-circle', 'check-circle'), ('fa-check-circle-o', 'check-circle-o'), ('fa-check-square', 'check-square'), ('fa-check-square-o', 'check-square-o'), ('fa-chevron-circle-down', 'chevron-circle-down'), ('fa-chevron-circle-left', 'chevron-circle-left'), ('fa-chevron-circle-right', 'chevron-circle-right'), ('fa-chevron-circle-up', 'chevron-circle-up'), ('fa-chevron-down', 'chevron-down'), ('fa-chevron-left', 'chevron-left'), ('fa-chevron-right', 'chevron-right'), ('fa-chevron-up', 'chevron-up'), ('fa-child', 'child'), ('fa-chrome', 'chrome'), ('fa-circle', 'circle'), ('fa-circle-o', 'circle-o'), ('fa-circle-o-notch', 'circle-o-notch'), ('fa-circle-thin', 'circle-thin'), ('fa-clipboard', 'clipboard'), ('fa-clock-o', 'clock-o'), ('fa-clone', 'clone'), ('fa-close', 'close'), ('fa-cloud', 'cloud'), ('fa-cloud-download', 'cloud-download'), ('fa-cloud-upload', 'cloud-upload'), ('fa-cny', 'cny'), ('fa-code', 'code'), ('fa-code-fork', 'code-fork'), ('fa-codepen', 'codepen'), ('fa-codiepie', 'codiepie'), ('fa-coffee', 'coffee'), ('fa-cog', 'cog'), ('fa-cogs', 'cogs'), ('fa-columns', 'columns'), ('fa-comment', 'comment'), ('fa-comment-o', 'comment-o'), ('fa-commenting', 'commenting'), ('fa-commenting-o', 'commenting-o'), ('fa-comments', 'comments'), ('fa-comments-o', 'comments-o'), ('fa-compass', 'compass'), ('fa-compress', 'compress'), ('fa-connectdevelop', 'connectdevelop'), ('fa-contao', 'contao'), ('fa-copy', 'copy'), ('fa-copyright', 'copyright'), ('fa-creative-commons', 'creative-commons'), ('fa-credit-card', 'credit-card'), ('fa-credit-card-alt', 'credit-card-alt'), ('fa-crop', 'crop'), ('fa-crosshairs', 'crosshairs'), ('fa-css3', 'css3'), ('fa-cube', 'cube'), ('fa-cubes', 'cubes'), ('fa-cut', 'cut'), ('fa-cutlery', 'cutlery'), ('fa-dashboard', 'dashboard'), ('fa-dashcube', 'dashcube'), ('fa-database', 'database'), ('fa-deaf', 'deaf'), ('fa-deafness', 'deafness'), ('fa-dedent', 'dedent'), ('fa-delicious', 'delicious'), ('fa-desktop', 'desktop'), ('fa-deviantart', 'deviantart'), ('fa-diamond', 'diamond'), ('fa-digg', 'digg'), ('fa-dollar', 'dollar'), ('fa-dot-circle-o', 'dot-circle-o'), ('fa-download', 'download'), ('fa-dribbble', 'dribbble'), ('fa-drivers-license', 'drivers-license'), ('fa-drivers-license-o', 'drivers-license-o'), ('fa-dropbox', 'dropbox'), ('fa-drupal', 'drupal'), ('fa-edge', 'edge'), ('fa-edit', 'edit'), ('fa-eercast', 'eercast'), ('fa-eject', 'eject'), ('fa-ellipsis-h', 'ellipsis-h'), ('fa-ellipsis-v', 'ellipsis-v'), ('fa-empire', 'empire'), ('fa-envelope', 'envelope'), ('fa-envelope-o', 'envelope-o'), ('fa-envelope-open', 'envelope-open'), ('fa-envelope-open-o', 'envelope-open-o'), ('fa-envelope-square', 'envelope-square'), ('fa-envira', 'envira'), ('fa-eraser', 'eraser'), ('fa-etsy', 'etsy'), ('fa-eur', 'eur'), ('fa-euro', 'euro'), ('fa-exchange', 'exchange'), ('fa-exclamation', 'exclamation'), ('fa-exclamation-circle', 'exclamation-circle'), ('fa-exclamation-triangle', 'exclamation-triangle'), ('fa-expand', 'expand'), ('fa-expeditedssl', 'expeditedssl'), ('fa-external-link', 'external-link'), ('fa-external-link-square', 'external-link-square'), ('fa-eye', 'eye'), ('fa-eye-slash', 'eye-slash'), ('fa-eyedropper', 'eyedropper'), ('fa-fa', 'fa'), ('fa-facebook', 'facebook'), ('fa-facebook-f', 'facebook-f'), ('fa-facebook-official', 'facebook-official'), ('fa-facebook-square', 'facebook-square'), ('fa-fast-backward', 'fast-backward'), ('fa-fast-forward', 'fast-forward'), ('fa-fax', 'fax'), ('fa-feed', 'feed'), ('fa-female', 'female'), ('fa-fighter-jet', 'fighter-jet'), ('fa-file', 'file'), ('fa-file-archive-o', 'file-archive-o'), ('fa-file-audio-o', 'file-audio-o'), ('fa-file-code-o', 'file-code-o'), ('fa-file-excel-o', 'file-excel-o'), ('fa-file-image-o', 'file-image-o'), ('fa-file-movie-o', 'file-movie-o'), ('fa-file-o', 'file-o'), ('fa-file-pdf-o', 'file-pdf-o'), ('fa-file-photo-o', 'file-photo-o'), ('fa-file-picture-o', 'file-picture-o'), ('fa-file-powerpoint-o', 'file-powerpoint-o'), ('fa-file-sound-o', 'file-sound-o'), ('fa-file-text', 'file-text'), ('fa-file-text-o', 'file-text-o'), ('fa-file-video-o', 'file-video-o'), ('fa-file-word-o', 'file-word-o'), ('fa-file-zip-o', 'file-zip-o'), ('fa-files-o', 'files-o'), ('fa-film', 'film'), ('fa-filter', 'filter'), ('fa-fire', 'fire'), ('fa-fire-extinguisher', 'fire-extinguisher'), ('fa-firefox', 'firefox'), ('fa-first-order', 'first-order'), ('fa-flag', 'flag'), ('fa-flag-checkered', 'flag-checkered'), ('fa-flag-o', 'flag-o'), ('fa-flash', 'flash'), ('fa-flask', 'flask'), ('fa-flickr', 'flickr'), ('fa-floppy-o', 'floppy-o'), ('fa-folder', 'folder'), ('fa-folder-o', 'folder-o'), ('fa-folder-open', 'folder-open'), ('fa-folder-open-o', 'folder-open-o'), ('fa-font', 'font'), ('fa-font-awesome', 'font-awesome'), ('fa-fonticons', 'fonticons'), ('fa-fort-awesome', 'fort-awesome'), ('fa-forumbee', 'forumbee'), ('fa-forward', 'forward'), ('fa-foursquare', 'foursquare'), ('fa-free-code-camp', 'free-code-camp'), ('fa-frown-o', 'frown-o'), ('fa-futbol-o', 'futbol-o'), ('fa-gamepad', 'gamepad'), ('fa-gavel', 'gavel'), ('fa-gbp', 'gbp'), ('fa-ge', 'ge'), ('fa-gear', 'gear'), ('fa-gears', 'gears'), ('fa-genderless', 'genderless'), ('fa-get-pocket', 'get-pocket'), ('fa-gg', 'gg'), ('fa-gg-circle', 'gg-circle'), ('fa-gift', 'gift'), ('fa-git', 'git'), ('fa-git-square', 'git-square'), ('fa-github', 'github'), ('fa-github-alt', 'github-alt'), ('fa-github-square', 'github-square'), ('fa-gitlab', 'gitlab'), ('fa-gittip', 'gittip'), ('fa-glass', 'glass'), ('fa-glide', 'glide'), ('fa-glide-g', 'glide-g'), ('fa-globe', 'globe'), ('fa-google', 'google'), ('fa-google-plus', 'google-plus'), ('fa-google-plus-circle', 'google-plus-circle'), ('fa-google-plus-official', 'google-plus-official'), ('fa-google-plus-square', 'google-plus-square'), ('fa-google-wallet', 'google-wallet'), ('fa-graduation-cap', 'graduation-cap'), ('fa-gratipay', 'gratipay'), ('fa-grav', 'grav'), ('fa-group', 'group'), ('fa-h-square', 'h-square'), ('fa-hacker-news', 'hacker-news'), ('fa-hand-grab-o', 'hand-grab-o'), ('fa-hand-lizard-o', 'hand-lizard-o'), ('fa-hand-o-down', 'hand-o-down'), ('fa-hand-o-left', 'hand-o-left'), ('fa-hand-o-right', 'hand-o-right'), ('fa-hand-o-up', 'hand-o-up'), ('fa-hand-paper-o', 'hand-paper-o'), ('fa-hand-peace-o', 'hand-peace-o'), ('fa-hand-pointer-o', 'hand-pointer-o'), ('fa-hand-rock-o', 'hand-rock-o'), ('fa-hand-scissors-o', 'hand-scissors-o'), ('fa-hand-spock-o', 'hand-spock-o'), ('fa-hand-stop-o', 'hand-stop-o'), ('fa-handshake-o', 'handshake-o'), ('fa-hard-of-hearing', 'hard-of-hearing'), ('fa-hashtag', 'hashtag'), ('fa-hdd-o', 'hdd-o'), ('fa-header', 'header'), ('fa-headphones', 'headphones'), ('fa-heart', 'heart'), ('fa-heart-o', 'heart-o'), ('fa-heartbeat', 'heartbeat'), ('fa-history', 'history'), ('fa-home', 'home'), ('fa-hospital-o', 'hospital-o'), ('fa-hotel', 'hotel'), ('fa-hourglass', 'hourglass'), ('fa-hourglass-1', 'hourglass-1'), ('fa-hourglass-2', 'hourglass-2'), ('fa-hourglass-3', 'hourglass-3'), ('fa-hourglass-end', 'hourglass-end'), ('fa-hourglass-half', 'hourglass-half'), ('fa-hourglass-o', 'hourglass-o'), ('fa-hourglass-start', 'hourglass-start'), ('fa-houzz', 'houzz'), ('fa-html5', 'html5'), ('fa-i-cursor', 'i-cursor'), ('fa-id-badge', 'id-badge'), ('fa-id-card', 'id-card'), ('fa-id-card-o', 'id-card-o'), ('fa-ils', 'ils'), ('fa-image', 'image'), ('fa-imdb', 'imdb'), ('fa-inbox', 'inbox'), ('fa-indent', 'indent'), ('fa-industry', 'industry'), ('fa-info', 'info'), ('fa-info-circle', 'info-circle'), ('fa-inr', 'inr'), ('fa-instagram', 'instagram'), ('fa-institution', 'institution'), ('fa-internet-explorer', 'internet-explorer'), ('fa-intersex', 'intersex'), ('fa-ioxhost', 'ioxhost'), ('fa-italic', 'italic'), ('fa-joomla', 'joomla'), ('fa-jpy', 'jpy'), ('fa-jsfiddle', 'jsfiddle'), ('fa-key', 'key'), ('fa-keyboard-o', 'keyboard-o'), ('fa-krw', 'krw'), ('fa-language', 'language'), ('fa-laptop', 'laptop'), ('fa-lastfm', 'lastfm'), ('fa-lastfm-square', 'lastfm-square'), ('fa-leaf', 'leaf'), ('fa-leanpub', 'leanpub'), ('fa-legal', 'legal'), ('fa-lemon-o', 'lemon-o'), ('fa-level-down', 'level-down'), ('fa-level-up', 'level-up'), ('fa-life-bouy', 'life-bouy'), ('fa-life-buoy', 'life-buoy'), ('fa-life-ring', 'life-ring'), ('fa-life-saver', 'life-saver'), ('fa-lightbulb-o', 'lightbulb-o'), ('fa-line-chart', 'line-chart'), ('fa-link', 'link'), ('fa-linkedin', 'linkedin'), ('fa-linkedin-square', 'linkedin-square'), ('fa-linode', 'linode'), ('fa-linux', 'linux'), ('fa-list', 'list'), ('fa-list-alt', 'list-alt'), ('fa-list-ol', 'list-ol'), ('fa-list-ul', 'list-ul'), ('fa-location-arrow', 'location-arrow'), ('fa-lock', 'lock'), ('fa-long-arrow-down', 'long-arrow-down'), ('fa-long-arrow-left', 'long-arrow-left'), ('fa-long-arrow-right', 'long-arrow-right'), ('fa-long-arrow-up', 'long-arrow-up'), ('fa-low-vision', 'low-vision'), ('fa-magic', 'magic'), ('fa-magnet', 'magnet'), ('fa-mail-forward', 'mail-forward'), ('fa-mail-reply', 'mail-reply'), ('fa-mail-reply-all', 'mail-reply-all'), ('fa-male', 'male'), ('fa-map', 'map'), ('fa-map-marker', 'map-marker'), ('fa-map-o', 'map-o'), ('fa-map-pin', 'map-pin'), ('fa-map-signs', 'map-signs'), ('fa-mars', 'mars'), ('fa-mars-double', 'mars-double'), ('fa-mars-stroke', 'mars-stroke'), ('fa-mars-stroke-h', 'mars-stroke-h'), ('fa-mars-stroke-v', 'mars-stroke-v'), ('fa-maxcdn', 'maxcdn'), ('fa-meanpath', 'meanpath'), ('fa-medium', 'medium'), ('fa-medkit', 'medkit'), ('fa-meetup', 'meetup'), ('fa-meh-o', 'meh-o'), ('fa-mercury', 'mercury'), ('fa-microchip', 'microchip'), ('fa-microphone', 'microphone'), ('fa-microphone-slash', 'microphone-slash'), ('fa-minus', 'minus'), ('fa-minus-circle', 'minus-circle'), ('fa-minus-square', 'minus-square'), ('fa-minus-square-o', 'minus-square-o'), ('fa-mixcloud', 'mixcloud'), ('fa-mobile', 'mobile'), ('fa-mobile-phone', 'mobile-phone'), ('fa-modx', 'modx'), ('fa-money', 'money'), ('fa-moon-o', 'moon-o'), ('fa-mortar-board', 'mortar-board'), ('fa-motorcycle', 'motorcycle'), ('fa-mouse-pointer', 'mouse-pointer'), ('fa-music', 'music'), ('fa-navicon', 'navicon'), ('fa-neuter', 'neuter'), ('fa-newspaper-o', 'newspaper-o'), ('fa-object-group', 'object-group'), ('fa-object-ungroup', 'object-ungroup'), ('fa-odnoklassniki', 'odnoklassniki'), ('fa-odnoklassniki-square', 'odnoklassniki-square'), ('fa-opencart', 'opencart'), ('fa-openid', 'openid'), ('fa-opera', 'opera'), ('fa-optin-monster', 'optin-monster'), ('fa-outdent', 'outdent'), ('fa-pagelines', 'pagelines'), ('fa-paint-brush', 'paint-brush'), ('fa-paper-plane', 'paper-plane'), ('fa-paper-plane-o', 'paper-plane-o'), ('fa-paperclip', 'paperclip'), ('fa-paragraph', 'paragraph'), ('fa-paste', 'paste'), ('fa-pause', 'pause'), ('fa-pause-circle', 'pause-circle'), ('fa-pause-circle-o', 'pause-circle-o'), ('fa-paw', 'paw'), ('fa-paypal', 'paypal'), ('fa-pencil', 'pencil'), ('fa-pencil-square', 'pencil-square'), ('fa-pencil-square-o', 'pencil-square-o'), ('fa-percent', 'percent'), ('fa-phone', 'phone'), ('fa-phone-square', 'phone-square'), ('fa-photo', 'photo'), ('fa-picture-o', 'picture-o'), ('fa-pie-chart', 'pie-chart'), ('fa-pied-piper', 'pied-piper'), ('fa-pied-piper-alt', 'pied-piper-alt'), ('fa-pied-piper-pp', 'pied-piper-pp'), ('fa-pinterest', 'pinterest'), ('fa-pinterest-p', 'pinterest-p'), ('fa-pinterest-square', 'pinterest-square'), ('fa-plane', 'plane'), ('fa-play', 'play'), ('fa-play-circle', 'play-circle'), ('fa-play-circle-o', 'play-circle-o'), ('fa-plug', 'plug'), ('fa-plus', 'plus'), ('fa-plus-circle', 'plus-circle'), ('fa-plus-square', 'plus-square'), ('fa-plus-square-o', 'plus-square-o'), ('fa-podcast', 'podcast'), ('fa-power-off', 'power-off'), ('fa-print', 'print'), ('fa-product-hunt', 'product-hunt'), ('fa-puzzle-piece', 'puzzle-piece'), ('fa-qq', 'qq'), ('fa-qrcode', 'qrcode'), ('fa-question', 'question'), ('fa-question-circle', 'question-circle'), ('fa-question-circle-o', 'question-circle-o'), ('fa-quora', 'quora'), ('fa-quote-left', 'quote-left'), ('fa-quote-right', 'quote-right'), ('fa-ra', 'ra'), ('fa-random', 'random'), ('fa-ravelry', 'ravelry'), ('fa-rebel', 'rebel'), ('fa-recycle', 'recycle'), ('fa-reddit', 'reddit'), ('fa-reddit-alien', 'reddit-alien'), ('fa-reddit-square', 'reddit-square'), ('fa-refresh', 'refresh'), ('fa-registered', 'registered'), ('fa-remove', 'remove'), ('fa-renren', 'renren'), ('fa-reorder', 'reorder'), ('fa-repeat', 'repeat'), ('fa-reply', 'reply'), ('fa-reply-all', 'reply-all'), ('fa-resistance', 'resistance'), ('fa-retweet', 'retweet'), ('fa-rmb', 'rmb'), ('fa-road', 'road'), ('fa-rocket', 'rocket'), ('fa-rotate-left', 'rotate-left'), ('fa-rotate-right', 'rotate-right'), ('fa-rouble', 'rouble'), ('fa-rss', 'rss'), ('fa-rss-square', 'rss-square'), ('fa-rub', 'rub'), ('fa-ruble', 'ruble'), ('fa-rupee', 'rupee'), ('fa-s15', 's15'), ('fa-safari', 'safari'), ('fa-save', 'save'), ('fa-scissors', 'scissors'), ('fa-scribd', 'scribd'), ('fa-search', 'search'), ('fa-search-minus', 'search-minus'), ('fa-search-plus', 'search-plus'), ('fa-sellsy', 'sellsy'), ('fa-send', 'send'), ('fa-send-o', 'send-o'), ('fa-server', 'server'), ('fa-share', 'share'), ('fa-share-alt', 'share-alt'), ('fa-share-alt-square', 'share-alt-square'), ('fa-share-square', 'share-square'), ('fa-share-square-o', 'share-square-o'), ('fa-shekel', 'shekel'), ('fa-sheqel', 'sheqel'), ('fa-shield', 'shield'), ('fa-ship', 'ship'), ('fa-shirtsinbulk', 'shirtsinbulk'), ('fa-shopping-bag', 'shopping-bag'), ('fa-shopping-basket', 'shopping-basket'), ('fa-shopping-cart', 'shopping-cart'), ('fa-shower', 'shower'), ('fa-sign-in', 'sign-in'), ('fa-sign-language', 'sign-language'), ('fa-sign-out', 'sign-out'), ('fa-signal', 'signal'), ('fa-signing', 'signing'), ('fa-simplybuilt', 'simplybuilt'), ('fa-sitemap', 'sitemap'), ('fa-skyatlas', 'skyatlas'), ('fa-skype', 'skype'), ('fa-slack', 'slack'), ('fa-sliders', 'sliders'), ('fa-slideshare', 'slideshare'), ('fa-smile-o', 'smile-o'), ('fa-snapchat', 'snapchat'), ('fa-snapchat-ghost', 'snapchat-ghost'), ('fa-snapchat-square', 'snapchat-square'), ('fa-snowflake-o', 'snowflake-o'), ('fa-soccer-ball-o', 'soccer-ball-o'), ('fa-sort', 'sort'), ('fa-sort-alpha-asc', 'sort-alpha-asc'), ('fa-sort-alpha-desc', 'sort-alpha-desc'), ('fa-sort-amount-asc', 'sort-amount-asc'), ('fa-sort-amount-desc', 'sort-amount-desc'), ('fa-sort-asc', 'sort-asc'), ('fa-sort-desc', 'sort-desc'), ('fa-sort-down', 'sort-down'), ('fa-sort-numeric-asc', 'sort-numeric-asc'), ('fa-sort-numeric-desc', 'sort-numeric-desc'), ('fa-sort-up', 'sort-up'), ('fa-soundcloud', 'soundcloud'), ('fa-space-shuttle', 'space-shuttle'), ('fa-spinner', 'spinner'), ('fa-spoon', 'spoon'), ('fa-spotify', 'spotify'), ('fa-square', 'square'), ('fa-square-o', 'square-o'), ('fa-stack-exchange', 'stack-exchange'), ('fa-stack-overflow', 'stack-overflow'), ('fa-star', 'star'), ('fa-star-half', 'star-half'), ('fa-star-half-empty', 'star-half-empty'), ('fa-star-half-full', 'star-half-full'), ('fa-star-half-o', 'star-half-o'), ('fa-star-o', 'star-o'), ('fa-steam', 'steam'), ('fa-steam-square', 'steam-square'), ('fa-step-backward', 'step-backward'), ('fa-step-forward', 'step-forward'), ('fa-stethoscope', 'stethoscope'), ('fa-sticky-note', 'sticky-note'), ('fa-sticky-note-o', 'sticky-note-o'), ('fa-stop', 'stop'), ('fa-stop-circle', 'stop-circle'), ('fa-stop-circle-o', 'stop-circle-o'), ('fa-street-view', 'street-view'), ('fa-strikethrough', 'strikethrough'), ('fa-stumbleupon', 'stumbleupon'), ('fa-stumbleupon-circle', 'stumbleupon-circle'), ('fa-subscript', 'subscript'), ('fa-subway', 'subway'), ('fa-suitcase', 'suitcase'), ('fa-sun-o', 'sun-o'), ('fa-superpowers', 'superpowers'), ('fa-superscript', 'superscript'), ('fa-support', 'support'), ('fa-table', 'table'), ('fa-tablet', 'tablet'), ('fa-tachometer', 'tachometer'), ('fa-tag', 'tag'), ('fa-tags', 'tags'), ('fa-tasks', 'tasks'), ('fa-taxi', 'taxi'), ('fa-telegram', 'telegram'), ('fa-television', 'television'), ('fa-tencent-weibo', 'tencent-weibo'), ('fa-terminal', 'terminal'), ('fa-text-height', 'text-height'), ('fa-text-width', 'text-width'), ('fa-th', 'th'), ('fa-th-large', 'th-large'), ('fa-th-list', 'th-list'), ('fa-themeisle', 'themeisle'), ('fa-thermometer', 'thermometer'), ('fa-thermometer-0', 'thermometer-0'), ('fa-thermometer-1', 'thermometer-1'), ('fa-thermometer-2', 'thermometer-2'), ('fa-thermometer-3', 'thermometer-3'), ('fa-thermometer-4', 'thermometer-4'), ('fa-thermometer-empty', 'thermometer-empty'), ('fa-thermometer-full', 'thermometer-full'), ('fa-thermometer-half', 'thermometer-half'), ('fa-thermometer-quarter', 'thermometer-quarter'), ('fa-thermometer-three-quarters', 'thermometer-three-quarters'), ('fa-thumb-tack', 'thumb-tack'), ('fa-thumbs-down', 'thumbs-down'), ('fa-thumbs-o-down', 'thumbs-o-down'), ('fa-thumbs-o-up', 'thumbs-o-up'), ('fa-thumbs-up', 'thumbs-up'), ('fa-ticket', 'ticket'), ('fa-times', 'times'), ('fa-times-circle', 'times-circle'), ('fa-times-circle-o', 'times-circle-o'), ('fa-times-rectangle', 'times-rectangle'), ('fa-times-rectangle-o', 'times-rectangle-o'), ('fa-tint', 'tint'), ('fa-toggle-down', 'toggle-down'), ('fa-toggle-left', 'toggle-left'), ('fa-toggle-off', 'toggle-off'), ('fa-toggle-on', 'toggle-on'), ('fa-toggle-right', 'toggle-right'), ('fa-toggle-up', 'toggle-up'), ('fa-trademark', 'trademark'), ('fa-train', 'train'), ('fa-transgender', 'transgender'), ('fa-transgender-alt', 'transgender-alt'), ('fa-trash', 'trash'), ('fa-trash-o', 'trash-o'), ('fa-tree', 'tree'), ('fa-trello', 'trello'), ('fa-tripadvisor', 'tripadvisor'), ('fa-trophy', 'trophy'), ('fa-truck', 'truck'), ('fa-try', 'try'), ('fa-tty', 'tty'), ('fa-tumblr', 'tumblr'), ('fa-tumblr-square', 'tumblr-square'), ('fa-turkish-lira', 'turkish-lira'), ('fa-tv', 'tv'), ('fa-twitch', 'twitch'), ('fa-twitter', 'twitter'), ('fa-twitter-square', 'twitter-square'), ('fa-umbrella', 'umbrella'), ('fa-underline', 'underline'), ('fa-undo', 'undo'), ('fa-universal-access', 'universal-access'), ('fa-university', 'university'), ('fa-unlink', 'unlink'), ('fa-unlock', 'unlock'), ('fa-unlock-alt', 'unlock-alt'), ('fa-unsorted', 'unsorted'), ('fa-upload', 'upload'), ('fa-usb', 'usb'), ('fa-usd', 'usd'), ('fa-user', 'user'), ('fa-user-circle', 'user-circle'), ('fa-user-circle-o', 'user-circle-o'), ('fa-user-md', 'user-md'), ('fa-user-o', 'user-o'), ('fa-user-plus', 'user-plus'), ('fa-user-secret', 'user-secret'), ('fa-user-times', 'user-times'), ('fa-users', 'users'), ('fa-vcard', 'vcard'), ('fa-vcard-o', 'vcard-o'), ('fa-venus', 'venus'), ('fa-venus-double', 'venus-double'), ('fa-venus-mars', 'venus-mars'), ('fa-viacoin', 'viacoin'), ('fa-viadeo', 'viadeo'), ('fa-viadeo-square', 'viadeo-square'), ('fa-video-camera', 'video-camera'), ('fa-vimeo', 'vimeo'), ('fa-vimeo-square', 'vimeo-square'), ('fa-vine', 'vine'), ('fa-vk', 'vk'), ('fa-volume-control-phone', 'volume-control-phone'), ('fa-volume-down', 'volume-down'), ('fa-volume-off', 'volume-off'), ('fa-volume-up', 'volume-up'), ('fa-warning', 'warning'), ('fa-wechat', 'wechat'), ('fa-weibo', 'weibo'), ('fa-weixin', 'weixin'), ('fa-whatsapp', 'whatsapp'), ('fa-wheelchair', 'wheelchair'), ('fa-wheelchair-alt', 'wheelchair-alt'), ('fa-wifi', 'wifi'), ('fa-wikipedia-w', 'wikipedia-w'), ('fa-window-close', 'window-close'), ('fa-window-close-o', 'window-close-o'), ('fa-window-maximize', 'window-maximize'), ('fa-window-minimize', 'window-minimize'), ('fa-window-restore', 'window-restore'), ('fa-windows', 'windows'), ('fa-won', 'won'), ('fa-wordpress', 'wordpress'), ('fa-wpbeginner', 'wpbeginner'), ('fa-wpexplorer', 'wpexplorer'), ('fa-wpforms', 'wpforms'), ('fa-wrench', 'wrench'), ('fa-xing', 'xing'), ('fa-xing-square', 'xing-square'), ('fa-y-combinator', 'y-combinator'), ('fa-y-combinator-square', 'y-combinator-square'), ('fa-yahoo', 'yahoo'), ('fa-yc', 'yc'), ('fa-yc-square', 'yc-square'), ('fa-yelp', 'yelp'), ('fa-yen', 'yen'), ('fa-yoast', 'yoast'), ('fa-youtube', 'youtube'), ('fa-youtube-play', 'youtube-play'), ('fa-youtube-square', 'youtube-square')])), ('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=5)), ('text', wagtail.core.blocks.TextBlock(help_text='Descripción'))])))])), ('projects', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10))])), ('testimonials', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Subtítulo', max_length=400, min_length=10)), ('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('author', wagtail.core.blocks.CharBlock(help_text='Autor', max_length=100, min_length=10)), ('author_position', wagtail.core.blocks.CharBlock(help_text='Posición del Autor', max_length=100, min_length=10, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(help_text='Texto', max_length=400, min_length=10))])))])), ('mobile_hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10)), ('text', wagtail.core.blocks.TextBlock(help_text='Texto')), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('laptop_hero', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10)), ('text', wagtail.core.blocks.TextBlock(help_text='Texto')), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('contact_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10)), ('button_title', wagtail.core.blocks.CharBlock(help_text='Titulo del Botón', max_length=70, min_length=10)), ('link', wagtail.core.blocks.PageChooserBlock())])), ('companies_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10))])), ('team_stack_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Subtítulo', max_length=400, min_length=10)), ('members', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('member', wagtail.core.blocks.CharBlock(help_text='Nombre del Miembro', max_length=100, min_length=3)), ('member_position', wagtail.core.blocks.CharBlock(help_text='Posición', max_length=100, min_length=3, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(help_text='Texto', max_length=600, min_length=10))])))])), ('contact_mobile_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Titulo', max_length=100, min_length=10)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='Subtítulo', max_length=200, min_length=10)), ('button_title', wagtail.core.blocks.CharBlock(help_text='Titulo del Botón', max_length=70, min_length=10)), ('link', wagtail.core.blocks.PageChooserBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))], null=True),
        ),
    ]
