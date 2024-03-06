FROM mcr.microsoft.com/dotnet/runtime:8.0 AS base
USER $APP_UID
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["Trackmania AI Trainer/Trackmania AI Trainer.csproj", "Trackmania AI Trainer/"]
RUN dotnet restore "Trackmania AI Trainer/Trackmania AI Trainer.csproj"
COPY . .
WORKDIR "/src/Trackmania AI Trainer"
RUN dotnet build "Trackmania AI Trainer.csproj" -c $BUILD_CONFIGURATION -o /app/build

FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "Trackmania AI Trainer.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Trackmania AI Trainer.dll"]
