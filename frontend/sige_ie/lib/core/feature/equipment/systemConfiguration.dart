import 'package:flutter/material.dart';
import 'package:sige_ie/config/app_styles.dart';
import 'package:sige_ie/core/feature/equipment/EquipmentScreen.dart';

class SystemConfiguration extends StatefulWidget {
  final String areaName;
  final String localName;
  final int localId;
  final int categoryNumber;

  const SystemConfiguration({
    super.key,
    required this.areaName,
    required this.localName,
    required this.localId,
    required this.categoryNumber,
  });

  @override
  _SystemConfigurationState createState() => _SystemConfigurationState();
}

class _SystemConfigurationState extends State<SystemConfiguration> {
  void navigateTo(String routeName, String areaName, String localName,
      int localId, dynamic category) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) {
          switch (routeName) {
            case '/structuredCabling':
            case '/atmosphericDischarges':
            case '/fireAlarm':
            case '/lighting':
            case '/electricLoads':
            case '/electricLines':
            case '/circuits':
            case '/distributionBoard':
            case '/cooling':
              return EquipmentScreen(
                  areaName: areaName,
                  localName: localName,
                  localId: localId,
                  categoryNumber: category);
            default:
              return Scaffold(
                body: Center(child: Text('No route defined for $routeName')),
              );
          }
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        backgroundColor: AppColors.sigeIeBlue,
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Container(
              width: double.infinity,
              padding: const EdgeInsets.fromLTRB(10, 10, 10, 35),
              decoration: const BoxDecoration(
                color: AppColors.sigeIeBlue,
                borderRadius:
                    BorderRadius.vertical(bottom: Radius.circular(20)),
              ),
              child: Center(
                child: Text(widget.areaName,
                    style: const TextStyle(
                        fontSize: 26,
                        fontWeight: FontWeight.bold,
                        color: Colors.white)),
              ),
            ),
            const Padding(
              padding: EdgeInsets.all(30.0),
              child: Text(
                'Quais sistemas deseja configurar?',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
            ),
            GridView.count(
              shrinkWrap: true,
              crossAxisCount: 3,
              childAspectRatio: 0.8, // Adjusted aspect ratio
              padding: const EdgeInsets.all(10.0),
              mainAxisSpacing: 10.0,
              crossAxisSpacing: 10.0,
              children: <Widget>[
                SystemIcon(
                  icon: Icons.fire_extinguisher,
                  label: 'ALARME DE INCÊNDIO',
                  onPressed: () => navigateTo('/fireAlarm', widget.areaName,
                      widget.localName, widget.localId, 8),
                ),
                SystemIcon(
                  icon: Icons.cable,
                  label: 'CABEAMENTO ESTRUTURADO',
                  onPressed: () => navigateTo('/structuredCabling',
                      widget.areaName, widget.localName, widget.localId, 6),
                ),
                SystemIcon(
                  icon: Icons.electrical_services,
                  label: 'CARGAS ELÉTRICAS',
                  onPressed: () => navigateTo('/electricLoads', widget.areaName,
                      widget.localName, widget.localId, 2),
                ),
                SystemIcon(
                  icon: Icons.electrical_services,
                  label: 'CIRCUITOS',
                  onPressed: () => navigateTo('/circuits', widget.areaName,
                      widget.localName, widget.localId, 4),
                ),
                SystemIcon(
                  icon: Icons.bolt,
                  label: 'DESCARGAS ATMOSFÉRICAS',
                  onPressed: () => navigateTo('/atmosphericDischarges',
                      widget.areaName, widget.localName, widget.localId, 7),
                ),
                SystemIcon(
                  icon: Icons.lightbulb,
                  label: 'ILUMINAÇÃO',
                  onPressed: () => navigateTo('/lighting', widget.areaName,
                      widget.localName, widget.localId, 1),
                ),
                SystemIcon(
                  icon: Icons.power,
                  label: 'LINHAS ELÉTRICAS',
                  onPressed: () => navigateTo('/electricLines', widget.areaName,
                      widget.localName, widget.localId, 3),
                ),
                SystemIcon(
                  icon: Icons.dashboard,
                  label: 'QUADRO DE DISTRIBUIÇÃO',
                  onPressed: () => navigateTo('/distributionBoard',
                      widget.areaName, widget.localName, widget.localId, 5),
                ),
                SystemIcon(
                  icon: Icons.ac_unit,
                  label: 'REFRIGERAÇÃO',
                  onPressed: () => navigateTo('/cooling', widget.areaName,
                      widget.localName, widget.localId, 9),
                ),
              ],
            ),
            const SizedBox(
              height: 30,
            ),
            Center(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      foregroundColor: AppColors.lightText,
                      backgroundColor: AppColors.warn,
                      minimumSize: const Size(150, 50),
                      textStyle: const TextStyle(
                        fontWeight: FontWeight.bold,
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8),
                      ),
                    ),
                    onPressed: () {
                      Navigator.of(context).popUntil((route) => route.isFirst);
                      Navigator.pushReplacementNamed(
                        context,
                        '/homeScreen',
                        arguments: {'initialPage': 1},
                      );
                    },
                    child: const Text('SAIR DA SALA'),
                  ),
                  const SizedBox(width: 10),
                  ElevatedButton(
                    style: ButtonStyle(
                      backgroundColor:
                          MaterialStateProperty.all(AppColors.sigeIeBlue),
                      foregroundColor:
                          MaterialStateProperty.all(AppColors.lightText),
                      minimumSize:
                          MaterialStateProperty.all(const Size(150, 50)),
                      shape: MaterialStateProperty.all(RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      )),
                    ),
                    onPressed: () {
                      Navigator.of(context).pushNamed('/arealocation',
                          arguments: {
                            'placeName': widget.localName,
                            'placeId': widget.localId
                          });
                    },
                    child: const Text(
                      'CRIAR NOVA SALA',
                      style:
                          TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(
              height: 30,
            ),
          ],
        ),
      ),
    );
  }
}

class SystemIcon extends StatelessWidget {
  final IconData icon;
  final String label;
  final VoidCallback onPressed;

  const SystemIcon({
    super.key,
    required this.icon,
    required this.label,
    required this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onPressed,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            width: 80,
            height: 80,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: AppColors.sigeIeYellow,
            ),
            child: Icon(
              icon,
              size: 40.0,
              color: AppColors.sigeIeBlue,
            ),
          ),
          const SizedBox(height: 10),
          Flexible(
            child: Text(
              label,
              textAlign: TextAlign.center,
              style: const TextStyle(
                color: AppColors.sigeIeBlue,
                fontSize: 12,
                fontWeight: FontWeight.bold,
              ),
              softWrap: true,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
          ),
        ],
      ),
    );
  }
}
