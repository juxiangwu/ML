/**
 * Created by sia on 5/13/16.
 */

sigma.utils.pkg('sigma.canvas.nodes');
sigma.canvas.nodes.image = (function () {
    var _cache = {},
        _loading = {},
        _callbacks = {};

    // Return the renderer itself:
    var renderer = function (node, context, settings) {
        var args = arguments,
            prefix = settings('prefix') || '',
            size = node[prefix + 'size'],
            color = node.color || settings('defaultNodeColor'),
            url = node.url;

        if (_cache[url]) {
            context.save();

            // Draw the clipping disc:
            context.beginPath();
            context.arc(
                node[prefix + 'x'],
                node[prefix + 'y'],
                node[prefix + 'size'],
                0,
                Math.PI * 2,
                true
            );
            context.closePath();
            context.clip();

            // Draw the image
            context.drawImage(
                _cache[url],
                node[prefix + 'x'] - size,
                node[prefix + 'y'] - size,
                2 * size,
                2 * size
            );

            // Quit the "clipping mode":
            context.restore();

            // Draw the border:
            context.beginPath();
            context.arc(
                node[prefix + 'x'],
                node[prefix + 'y'],
                node[prefix + 'size'],
                0,
                Math.PI * 2,
                true
            );
            context.lineWidth = size / 5;
            context.strokeStyle = node.color || settings('defaultNodeColor');
            context.stroke();
        } else {
            sigma.canvas.nodes.image.cache(url);
            sigma.canvas.nodes.def.apply(
                sigma.canvas.nodes,
                args
            );
        }
    };

    // Let's add a public method to cache images, to make it possible to
    // preload images before the initial rendering:
    renderer.cache = function (url, callback) {
        if (callback)
            _callbacks[url] = callback;

        if (_loading[url])
            return;

        var img = new Image();

        img.onload = function () {
            _loading[url] = false;
            _cache[url] = img;

            if (_callbacks[url]) {
                _callbacks[url].call(this, img);
                delete _callbacks[url];
            }
        };

        _loading[url] = true;
        img.src = url;
    };

    return renderer;
})();

// Now that's the renderer has been implemented, let's generate a graph
// to render:
var i,
    s,
    img,
    N = 8,
    E = 13,
    g = {
        nodes: [],
        edges: []
    },
    urls = [
        'img/plus_sym.jpg',
        'img/sub_sym.png'
    ],
    loaded = 0,
    colors = [
        '#ffffff',
        '#617db4',
        '#668f3c', // Green
        '#c6583e', // Red
        '#b956af' // Purple
    ];

// Nodes
g.nodes.push({
    id: 'n0',
    type: 'image',
    url: urls[0],
    x: Math.random(),
    y: Math.random(),
    size: 20,
    color: colors[3]
});
g.nodes.push({
    id: 'n1',
    type: 'image',
    url: urls[0],
    x: Math.random(),
    y: Math.random(),
    size: 20,
    color: colors[3]
});
g.nodes.push({
    id: 'n2',
    type: 'image',
    url: urls[1],
    x: Math.random(),
    y: Math.random(),
    size: 20,
    color: colors[3]
});

// Edges
g.edges.push({
    id: 'e0',
    source: 'n0',
    target: 'n2',
    size: 20
});
g.edges.push({
    id: 'e1',
    source: 'n1',
    target: 'n2',
    size: 20
});

// Generate a random graph, with ~30% nodes having the type "image":
//    for (i = 0; i < N; i++) {
//        img = Math.random() >= 0.7;
//        g.nodes.push({
//            id: 'n' + i,
//            label: 'Node ' + i,
//            type: img ? 'image' : 'def',
//            url: img ? urls[Math.floor(Math.random() * urls.length)] : null,
//            x: Math.random(),
//            y: Math.random(),
//            size: Math.random(),
//            color: colors[Math.floor(Math.random() * colors.length)]
//        });
//    }

//    for (i = 0; i < E; i++)
//        g.edges.push({
//            id: 'e' + i,
//            source: 'n' + (Math.random() * N | 0),
//            target: 'n' + (Math.random() * N | 0),
//            size: Math.random()
//        });

// Then, wait for all images to be loaded before instanciating sigma:
urls.forEach(function (url) {
    sigma.canvas.nodes.image.cache(
        url,
        function () {
            if (++loaded === urls.length)
            // Instantiate sigma:
                s = new sigma({
                    graph: g,
                    renderer: {
                        // IMPORTANT:
                        // This works only with the canvas renderer, so the
                        // renderer type set as "canvas" is necessary here.
                        container: document.getElementById('graph-container'),
                        type: 'canvas'
                    },
                    settings: {
                        minNodeSize: 8,
                        maxNodeSize: 16
                    }
                });
        }
    );
});