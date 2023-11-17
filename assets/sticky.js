window.dash_props = Object.assign({}, window.dash_props, {
    module: {
        on_each_feature: function(feature, layer, context) {
            if (!feature.properties) {
                return
            }
            if (feature.properties.popup) {
                layer.bindPopup(feature.properties.popup)
            }
            if (feature.properties.tooltip) {
                // here you can change all leaflet tooltip options
                layer.bindTooltip(feature.properties.tooltip, { opacity: 1.0 ,sticky:true})
                layer.on('click', function () {
                    layer.closeTooltip();
                });                
            }
        }
    }
});