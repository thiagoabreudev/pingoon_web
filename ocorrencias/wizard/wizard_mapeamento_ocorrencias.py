#!/usr/bin/python
# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields

class wizard_ocorrencia_mapeamento(osv.TransientModel):
    _name = 'wizard.ocorrencia.mapeamento'
    _columns = {
        'ocorrencia_status': fields.char('Status')
    }

    def button_gerar_mapa(self, cr, uid, ids, context):
        obj_ocorrencia = self.pool.get('ocorrencia')
        ocorrencia_ids = obj_ocorrencia.search(cr, uid, [])
        ocorrencia_dados = obj_ocorrencia.read(cr, uid, ocorrencia_ids, ['id',
                                                                         'ocorrencia_latitude',
                                                                         'ocorrencia_longitude',
                                                                         'state'])
        markers = []
        cont = 0
        latlon = False
        for dado in ocorrencia_dados:
            if dado.get('ocorrencia_latitude') != "SEM LATITUDE"\
                    and dado.get('ocorrencia_longitude') != "SEM LONGITUDE":
                if cont == 0:
                    lon = str(dado.get('ocorrencia_longitude'))
                    lon = lon.split('.')[0] + '.' + lon.split('.')[1][:2]
                    lat = str(dado.get('ocorrencia_latitude'))
                    lat = lat.split('.')[0] + '.' + lat.split('.')[1][:2]
                    latlon = (lat, lon)
                cont += 1
                icon = self.get_icon_state(dado.get('state'))
                markers.append([
                    str(dado.get('id')),
                    str(dado.get('ocorrencia_latitude')),
                    str(dado.get('ocorrencia_longitude')),
                    cont,
                    icon])
        self.gerar_html_mapa(markers, latlon)
        # url = 'http://52.25.81.7/mapas/mapa.html'
        url = 'http://localhost/mapas/mapa.html'
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }

    @staticmethod
    def get_icon_state(state):
        icon = ''
        if state == '1':
            icon = 'blue-dot.png'
        elif state == '2':
            icon = 'ltblue-dot.png'
        elif state == '3':
            icon = 'orange-dot.png'
        elif state == '4':
            icon = 'yellow-dot.png'
        elif state == '5':
            icon = 'red-dot.png'
        return icon

    @staticmethod
    def gerar_html_mapa(markers, latlon):
        html = """
                <!DOCTYPE html>
                <html>
                <head>
                    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
                    <title>Google Maps Multiple Markers</title>
                    <script src="http://maps.google.com/maps/api/js?sensor=false"
                            type="text/javascript"></script>
                </head>
                <body>
                <div id="map" style="width: 100%; height: 768px;"></div>

                <script type="text/javascript">
                    var locations = """ + str(markers) + """;

                    var map = new google.maps.Map(document.getElementById('map'), {
                        zoom: 10,
                        center: new google.maps.LatLng""" + str(latlon) + """,
                        mapTypeId: google.maps.MapTypeId.ROADMAP
                    });

                    var infowindow = new google.maps.InfoWindow();

                    var marker, i;

                    for (i = 0; i < locations.length; i++) {
                        icon = 'http://maps.google.com/mapfiles/ms/icons/' + locations[i][4];
                        marker = new google.maps.Marker({
                            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                            map: map,
                            icon: icon,
                        });

                        google.maps.event.addListener(marker, 'click', (function(marker, i) {
                            return function() {
                                infowindow.setContent(locations[i][0]);
                                infowindow.open(map, marker);
                            }
                        })(marker, i));
                    }
                </script>
                </body>
                </html>
        """
        arquivo = open('/var/www/mapas/mapa.html', 'wb')
        arquivo.writelines(html)
        arquivo.close()
        return True