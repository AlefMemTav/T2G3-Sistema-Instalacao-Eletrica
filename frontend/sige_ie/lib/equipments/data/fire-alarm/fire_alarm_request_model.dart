class FireAlarmRequestModel {
  int? area;
  int? system;

  FireAlarmRequestModel({
    required this.area,
    required this.system,
  });

  Map<String, dynamic> toJson() {
    return {
      'area': area,
      'system': system,
    };
  }
}
