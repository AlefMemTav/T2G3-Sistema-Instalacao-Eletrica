import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:http_interceptor/http_interceptor.dart';
import 'package:sige_ie/core/data/auth_interceptor.dart';
import 'package:sige_ie/main.dart';
import 'package:sige_ie/users/data/user_model.dart';

class UserService {
  static Future<bool> register(
      String username, String firstName, String password, String email) async {
    //var csrfToken = await AuthService.fetchCsrfToken();
    var url = Uri.parse('http://10.0.2.2:8000/api/users/');
    try {
      var response = await http.post(url,
          headers: {'Content-Type': 'application/json'},
          body: jsonEncode({
            'username': username,
            'first_name': firstName,
            'password': password,
            'email': email,
          }));
      if (response.statusCode == 200 || response.statusCode == 201) {
        var data = jsonDecode(response.body);
        print("Registro bem-sucedido: $data");
        return true;
      } else {
        print("Falha no registro: ${response.body}");
        return false;
      }
    } catch (e) {
      print("Erro ao tentar registrar: $e");
      return false;
    }
  }

  Future<bool> update(String id, String firstName, String email) async {
    var client = InterceptedClient.build(
      interceptors: [AuthInterceptor(cookieJar)],
    );

    //var csrfToken = await AuthService.fetchCsrfToken();

    var url = Uri.parse('http://10.0.2.2:8000/api/users/$id/');
    try {
      var response = await client.put(url,
          headers: {'Content-Type': 'application/json'},
          body: jsonEncode({
            'first_name': firstName,
            'email': email,
          }));
      if (response.statusCode == 200 || response.statusCode == 201) {
        var data = jsonDecode(response.body);
        print("Atualizado com sucesso: $data");
        return true;
      } else {
        print("Falha: ${response.body}");
        return false;
      }
    } catch (e) {
      print("Erro ao tentar registrar: $e");
      return false;
    }
  }

  Future<bool> delete(String id) async {
    var client = InterceptedClient.build(
      interceptors: [AuthInterceptor(cookieJar)],
    );

    //var csrfToken = await AuthService.fetchCsrfToken();

    var url = Uri.parse('http://10.0.2.2:8000/api/users/$id/');
    try {
      var response =
          await client.delete(url, headers: {'Content-Type': 'application/json'});
      if (response.statusCode == 204) {
        var data = jsonDecode(response.body);
        print("Excluido com sucesso: $data");
        return true;
      } else {
        print("Falha: ${response.body}");
        return false;
      }
    } catch (e) {
      print("Erro ao tentar excluir: $e");
      return false;
    }
  }

  Future<UserModel> fetchProfileData() async {
    var client = InterceptedClient.build(
      interceptors: [AuthInterceptor(cookieJar)],
    );

    final response =
        await client.get(Uri.parse('http://10.0.2.2:8000/api/userauth'));

    if (response.statusCode == 200) {
      var data = jsonDecode(response.body);
      return UserModel.fromJson(data);
    } else {
      throw Exception('Falha ao carregar dados do perfil');
    }
  }
}
