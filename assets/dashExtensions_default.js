window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(feature, context) {
            const {
                classes,
                colorscale,
                style,
                colorProp
            } = context.props.hideout;
            const value = feature.properties[colorProp];
            if (value === null || isNaN(value)) {
                // Asigna color gris para observaciones sin datos
                style.fillColor = 'rgb(128, 128, 128)';
                style.weight = 1;
                style.dashArray = false;
            } else {
                for (let i = 0; i <= classes.length; ++i) {
                    if (value >= classes[i]) {
                        style.fillColor = colorscale[i];
                        style.weight = 1;
                        style.dashArray = false;
                    }
                }
            }
            return style;
        }
    }
});