const Loading = ({ message = "加载中...", size = "default", variant = "default" }) => {
  const sizeClasses = {
    small: "w-4 h-4",
    default: "w-6 h-6",
    large: "w-8 h-8"
  };

  const spinnerClasses = {
    default: "border-primary-200 border-t-primary-600",
    light: "border-white border-opacity-30 border-t-white",
  };

  const textClasses = {
    default: "text-gray-600",
    light: "text-white",
  };

  return (
    <div className="flex items-center justify-center gap-2">
      <div className={`${sizeClasses[size]} border-2 ${spinnerClasses[variant]} rounded-full animate-spin`}></div>
      <span className={textClasses[variant]}>{message}</span>
    </div>
  );
};

export default Loading;