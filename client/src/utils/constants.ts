import firebase from 'firebase/app'
import { Dispatch } from 'react'

interface CoinCoinUser {
    uid: string,
    email: string,
    displayName: string,
    coinVal: string,
    photoURL: string
}

export type State = {
    authData: CoinCoinUser
}

export interface Context {
    state: State
    dispatch: Dispatch<Action>
}

export enum ActionKind {
    signIn = 'AUTHENTICATE',
    signOut = "LOGOUT",
}

export type Action = {
    type: ActionKind,
    payload: CoinCoinUser
}

export const signInAction = (user: CoinCoinUser): Action => ({
    type: ActionKind.signIn,
    payload: user,
})

export const signOutAction: Action = {
    type: ActionKind.signOut,
    payload: null,
}