import firebase from 'firebase/app';
import 'firebase/auth';

export const firebaseConfig = {
    apiKey: "AIzaSyArSCCKKt5x4Ih5SrI8-JPEWdkWTyLum9w",
    authDomain: "coincoin-310916.firebaseapp.com",
    projectId: "coincoin-310916",
    storageBucket: "coincoin-310916.appspot.com",
    messagingSenderId: "316284443889",
    appId: "1:316284443889:web:1e126a7fe3b8edcf381d50"
};

if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}


export const auth = firebase.auth();

const provider = new firebase.auth.GoogleAuthProvider();
provider.setCustomParameters({ prompt: 'select_account' });
provider.addScope('email')
provider.addScope('profile')
export const signInWithGoogle = () => auth.signInWithPopup(provider);

auth.onAuthStateChanged((user) => {})

export default firebase;