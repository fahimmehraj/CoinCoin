import NavigationBar from '../components/navbar'

import type { AppProps } from 'next/app'

import '../styles/globals.css'
import Footer from '../components/Footer'
import Store, { useAuth } from '../utils/context/store'
import { useEffect } from 'react'
import { signInAction } from '../utils/constants'
import { auth } from '../utils/firebase.utils'
import { ApolloProvider } from '@apollo/client'
import client from '../utils/apollo-client'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ApolloProvider client={client}>
      <Store>

        <div className="relative h-screen bg-gray-100">
          <NavigationBar />
          <Component {...pageProps} />
          <Footer />
        </div>

      </Store>
    </ApolloProvider>
  )
}

export default MyApp
