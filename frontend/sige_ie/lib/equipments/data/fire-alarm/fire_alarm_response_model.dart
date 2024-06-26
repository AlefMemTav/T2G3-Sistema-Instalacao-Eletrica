class FireAlarmEquipmentResponseModel {
  int id;
  String area;
  int system;

  FireAlarmEquipmentResponseModel({
    required this.id,
    required this.area,
    required this.system,
  });

  factory FireAlarmEquipmentResponseModel.fromJson(Map<String, dynamic> json) {
    return FireAlarmEquipmentResponseModel(
      id: json['id'],
      area: json['name'],
      system: json['system'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'area': area,
      'system': system,
    };
  }
}
