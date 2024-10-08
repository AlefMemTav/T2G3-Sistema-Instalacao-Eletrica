class RefrigerationsResponseModel {
  int id;
  int area;
  int equipment;
  int system;
  int quantity;
  int power;
  String? observation;

  RefrigerationsResponseModel(
      {required this.id,
      required this.area,
      required this.equipment,
      required this.system,
      required this.quantity,
      required this.power,
      required this.observation});

  factory RefrigerationsResponseModel.fromJson(Map<String, dynamic> json) {
    return RefrigerationsResponseModel(
        id: json['id'],
        area: json['area'],
        equipment: json['equipment'],
        system: json['system'],
        quantity: json['quantity'],
        power: json['power'],
        observation: json['observation']);
  }
}
