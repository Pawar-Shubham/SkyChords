import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import React from 'react';
import home from './Screens//home';
import login from './Screens/login';
import signup from './Screens/signup';
import forgotpass from './Screens/forgotpass';
import index from './Screens/index';
import saved from './Screens/saved';
import otp from './Screens/otp';
import ip from './Screens/ip';

const stack = createStackNavigator();
const Stacknavigator = () => {
  return (
    <stack.Navigator>
      <stack.Screen
        options={{headerShown: false}}
        name="main"
        component={home}
      />
      <stack.Screen
        options={{
          title: 'Log in',
          headerStyle: {backgroundColor: '#0096FF'},
        }}
        name="login"
        component={login}
      />
      <stack.Screen
        options={{
          title: 'Sign up',
          headerStyle: {backgroundColor: '#0096FF'},
        }}
        name="signup"
        component={signup}
      />
      <stack.Screen
        options={{
          title: 'Forgot pass',
          headerStyle: {backgroundColor: '#0096FF'},
        }}
        name="forgotpass"
        component={forgotpass}
      />
      <stack.Screen
        options={{
          title: 'Saved',
          headerStyle: {backgroundColor: '#0096FF'},
        }}
        name="saved"
        component={saved}
      />
      <stack.Screen
        options={{
          title: 'Generate chords',
          headerStyle: {backgroundColor: '#0096FF'},
        }}
        name="index"
        component={index}
      />
      <stack.Screen
        options={{
          title: 'Enter Your OTP',
          headerStyle: {backgroundColor: '#0096FF'},
        }}
        name="otp"
        component={otp}
      />
      <stack.Screen
        options={{
          title: 'Ip',
          headerStyle: {backgroundColor: '#0096FF'},
        }}
        name="ip"
        component={ip}
      />
    </stack.Navigator>
  );
};

export default () => {
  return (
    <NavigationContainer>
      <Stacknavigator />
    </NavigationContainer>
  );
};
