import 'package:flutter/material.dart';

class AppColors {
  static const Color sigeIeYellow = Color(0xFFF1F60E);
  static const Color sigeIeBlue = Color(0xff123c75);
  static const Color dartText = Color.fromRGBO(22, 22, 22, 1);
  static const Color lightText = Color.fromARGB(255, 233, 226, 226);
  static const Color warn = Color.fromARGB(255, 231, 27, 27);
  static const Color accent = Color.fromARGB(255, 231, 85, 27);
}

class AppButtonStyles {
  static ButtonStyle warnButton = ElevatedButton.styleFrom(
    backgroundColor: Color.fromARGB(255, 231, 27, 27),
    minimumSize: Size(150, 50),
  );
  static ButtonStyle accentButton = ElevatedButton.styleFrom(
    backgroundColor: Color.fromARGB(255, 231, 85, 27),
    minimumSize: Size(150, 50),
  );
}