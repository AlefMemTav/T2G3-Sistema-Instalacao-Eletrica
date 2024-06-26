import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:http_interceptor/http_interceptor.dart';
import 'package:sige_ie/core/data/auth_interceptor.dart';
import 'package:sige_ie/equipments/data/fire-alarm/fire_alarm_equipment_request_model.dart';
import 'package:sige_ie/main.dart';

class EquipmentService {
  final String baseUrl = 'http://10.0.2.2:8000/api/equipment-details/';
  http.Client client = InterceptedClient.build(
    interceptors: [AuthInterceptor(cookieJar)],
  );

  Future<bool> createFireAlarm(
      FireAlarmEquipmentRequestModel
          fireAlarmEquipmentRequestModel) async {
    var url = Uri.parse(baseUrl);

    try {
      var response = await client.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(fireAlarmEquipmentRequestModel.toJson()),
      );

      print('Response status code: ${response.statusCode}');
      print('Response body: ${response.body}');

      if (response.statusCode == 201) {
        Map<String, dynamic> responseData = jsonDecode(response.body);
        print('Request successful, received ID: ${responseData['id']}');
        return true;
      } else {
        print(
            'Failed to register fire alarm equipment: ${response.statusCode}');
        return false;
      }
    } catch (e) {
      print('Error during register: $e');
      return false;
    }
  }
}
