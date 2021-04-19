import { gql, useQuery } from "@apollo/client";
import React, { createContext, useContext, useEffect, useReducer } from "react";
import client from "../apollo-client";
import { Context as StateContext, signInAction, signOutAction, State } from "../constants";
import { auth } from "../firebase.utils";
import Reducer from './reducer'


const initialState: State = {
    authData: null,
};

const checkUser = gql`
query getUserbyID($uid: String!) {
    getUserbyID(userID: $uid) {
        coinVal
    }
  }
`;

const createUser = gql`
mutation createUser($uid: String!, $email: String!, $displayName: String!) {
    createUser(userID: $uid, email: $email, displayName: $displayName, coinVal: 0) {
      user {
        coinVal
        displayName
      }
    }
  }
  
`;

const Store = ({ children }) => {
    useEffect(() => {
        auth.onAuthStateChanged(async (user) => {
            if (user) {
                const { error, loading, data } = await client.query({ query: checkUser, variables: { uid: user.uid } })
                console.log('data')
                console.log(data)
                if (data.getUserbyID.coinVal === null) {
                    console.log('yeh its null')
                    const { data: newData } = await client.mutate({ mutation: createUser, variables: { uid: user.uid, email: user.email, displayName: user.displayName } })
                    console.log(newData.coinVal)
                    const coinCoinUser = { uid: user.uid, email: user.email, displayName: user.displayName, coinVal: newData.getUserbyID.coinVal, photoURL: user.photoURL }
                    console.log(coinCoinUser)
                    dispatch(signInAction(coinCoinUser))
                } else {
                    console.log('nah u good')
                    console.log(data.getUserbyID.coinVal)
                    dispatch(signInAction({ uid: user.uid, email: user.email, displayName: user.displayName, coinVal: data.getUserbyID.coinVal, photoURL: user.photoURL }))
                }
            } else {
                dispatch(signOutAction)
            }
        })
    }, [])

    const [state, dispatch] = useReducer(Reducer, initialState);
    return (

        <Context.Provider value={{ state, dispatch }}>
            {children}
        </Context.Provider>
    )
};

export const Context = createContext<StateContext>({ state: initialState, dispatch: (action) => console.log("hi") });
export const useAuth = () => useContext(Context)
export default Store;