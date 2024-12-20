"use client";

import { useGoogleLogin } from "@react-oauth/google";

const LoginPage = (handleGoogleSignIn: React.FC) => {
  const login = useGoogleLogin({
    onSuccess: (tokenResponse) => handleGoogleSignIn(tokenResponse),
  });
  return (
    <>
      <button onClick={() => login()} className="border rounded-lg px-4 py-2">
        Signin with Google
      </button>
    </>
  );
};
export default LoginPage;
