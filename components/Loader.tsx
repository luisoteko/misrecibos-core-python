import { MutatingDots } from "react-loader-spinner";

export default function Loader({ visible }: Readonly<{ visible: boolean }>) {
  return (
    <>
      {visible && (
        <div className="fixed top-0 left-0 z-50 w-full h-full bg-gray-800 bg-opacity-50 flex items-center justify-center">
          <MutatingDots
            visible={visible}
            height="100"
            width="100"
            color="#1d4fd8"
            secondaryColor="#3b82f6"
            radius="15"
            ariaLabel="Cargando..."
          />
        </div>
      )}
    </>
  );
}
