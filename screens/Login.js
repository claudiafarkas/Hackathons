import React, { Component } from "react";
import { StyleSheet, Button, View, SafeAreaView, Text, Alert } from 'react-native';

export default function Login({navigation}) {
  return (
    <SafeAreaView style={styles.container}>
      <Text>Login screen</Text>
      <Button
        title="Login"
        onPress={() => navigation.navigate('ProfileStack')}
      />
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
