import { gql, useQuery } from "@apollo/client";
import React, {createContext, useContext, useEffect, useReducer} from "react";
import client from "../apollo-client";
import { Context as StateContext, signInAction, signOutAction, State } from "../constants";
import { auth } from "../firebase.utils";
import Reducer from './reducer'


const initialState: State = {
    authData: null,
};

const checkUser = gql`
  query {
    getUser(userID: $uid)
  }
`;

const Store = ({children}) => {
    useEffect(() => {
        auth.onAuthStateChanged(async(user) => {
            if (user) {
                dispatch(signInAction(user))
                console.log(process.env.NEXT_PUBLIC_GRAPHQL_ENDPOINT)
                const data = await client.query({ query: checkUser, variables: { uid: "veryrealkey" }})
                console.log(data)
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

export const Context = createContext<StateContext>({ state: initialState, dispatch: (action) => console.log("hi")});
export const useAuth = () => useContext(Context)
export default Store;