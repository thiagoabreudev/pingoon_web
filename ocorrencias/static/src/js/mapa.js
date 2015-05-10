openerp.ocorrencias = function(instance, local) {
    alert("TESTTE");
    var _t = openerp.web._t,
        _lt = openerp.web._lt;
    var QWeb = openerp.web.qweb;

    local.HomePage = instance.Widget.extend({
        start: function() {
            alert("aqui tabm");
            console.log("pet store home page loaded");
        },
    });

    openerp.web.client_actions.add(
        'ocorrencia_mapa', 'local.HomePage');
}