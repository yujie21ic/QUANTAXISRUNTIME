// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: quotation.proto
#pragma warning disable 1591
#region Designer generated code

using System;
using System.Threading;
using System.Threading.Tasks;
using grpc = global::Grpc.Core;

namespace QUANTAXISRuntimeQuotation {
  public static partial class StockHQService
  {
    static readonly string __ServiceName = "QUANTAXIS_Runtime_Quotation.StockHQService";

    static readonly grpc::Marshaller<global::QUANTAXISRuntimeQuotation.query_struct> __Marshaller_query_struct = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::QUANTAXISRuntimeQuotation.query_struct.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::QUANTAXISRuntimeQuotation.hq_struct> __Marshaller_hq_struct = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::QUANTAXISRuntimeQuotation.hq_struct.Parser.ParseFrom);

    static readonly grpc::Method<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct> __Method_QA_fetch_p2p = new grpc::Method<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct>(
        grpc::MethodType.Unary,
        __ServiceName,
        "QA_fetch_p2p",
        __Marshaller_query_struct,
        __Marshaller_hq_struct);

    static readonly grpc::Method<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct> __Method_QA_fetch_p2s = new grpc::Method<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct>(
        grpc::MethodType.ServerStreaming,
        __ServiceName,
        "QA_fetch_p2s",
        __Marshaller_query_struct,
        __Marshaller_hq_struct);

    static readonly grpc::Method<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct> __Method_QA_fetch_s2s = new grpc::Method<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct>(
        grpc::MethodType.DuplexStreaming,
        __ServiceName,
        "QA_fetch_s2s",
        __Marshaller_query_struct,
        __Marshaller_hq_struct);

    static readonly grpc::Method<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct> __Method_QA_fetch_s2p = new grpc::Method<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct>(
        grpc::MethodType.ClientStreaming,
        __ServiceName,
        "QA_fetch_s2p",
        __Marshaller_query_struct,
        __Marshaller_hq_struct);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::QUANTAXISRuntimeQuotation.QuotationReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of StockHQService</summary>
    public abstract partial class StockHQServiceBase
    {
      public virtual global::System.Threading.Tasks.Task<global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_p2p(global::QUANTAXISRuntimeQuotation.query_struct request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task QA_fetch_p2s(global::QUANTAXISRuntimeQuotation.query_struct request, grpc::IServerStreamWriter<global::QUANTAXISRuntimeQuotation.hq_struct> responseStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task QA_fetch_s2s(grpc::IAsyncStreamReader<global::QUANTAXISRuntimeQuotation.query_struct> requestStream, grpc::IServerStreamWriter<global::QUANTAXISRuntimeQuotation.hq_struct> responseStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      /// <summary>
      ///rpc RouteChat (stream long) returns (stream long_hq);
      /// </summary>
      /// <param name="requestStream">Used for reading requests from the client.</param>
      /// <param name="context">The context of the server-side call handler being invoked.</param>
      /// <returns>The response to send back to the client (wrapped by a task).</returns>
      public virtual global::System.Threading.Tasks.Task<global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_s2p(grpc::IAsyncStreamReader<global::QUANTAXISRuntimeQuotation.query_struct> requestStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for StockHQService</summary>
    public partial class StockHQServiceClient : grpc::ClientBase<StockHQServiceClient>
    {
      /// <summary>Creates a new client for StockHQService</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public StockHQServiceClient(grpc::Channel channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for StockHQService that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public StockHQServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected StockHQServiceClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected StockHQServiceClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual global::QUANTAXISRuntimeQuotation.hq_struct QA_fetch_p2p(global::QUANTAXISRuntimeQuotation.query_struct request, grpc::Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return QA_fetch_p2p(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::QUANTAXISRuntimeQuotation.hq_struct QA_fetch_p2p(global::QUANTAXISRuntimeQuotation.query_struct request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_QA_fetch_p2p, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_p2pAsync(global::QUANTAXISRuntimeQuotation.query_struct request, grpc::Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return QA_fetch_p2pAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_p2pAsync(global::QUANTAXISRuntimeQuotation.query_struct request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_QA_fetch_p2p, null, options, request);
      }
      public virtual grpc::AsyncServerStreamingCall<global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_p2s(global::QUANTAXISRuntimeQuotation.query_struct request, grpc::Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return QA_fetch_p2s(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncServerStreamingCall<global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_p2s(global::QUANTAXISRuntimeQuotation.query_struct request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncServerStreamingCall(__Method_QA_fetch_p2s, null, options, request);
      }
      public virtual grpc::AsyncDuplexStreamingCall<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_s2s(grpc::Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return QA_fetch_s2s(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncDuplexStreamingCall<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_s2s(grpc::CallOptions options)
      {
        return CallInvoker.AsyncDuplexStreamingCall(__Method_QA_fetch_s2s, null, options);
      }
      /// <summary>
      ///rpc RouteChat (stream long) returns (stream long_hq);
      /// </summary>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      public virtual grpc::AsyncClientStreamingCall<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_s2p(grpc::Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return QA_fetch_s2p(new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      ///rpc RouteChat (stream long) returns (stream long_hq);
      /// </summary>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      public virtual grpc::AsyncClientStreamingCall<global::QUANTAXISRuntimeQuotation.query_struct, global::QUANTAXISRuntimeQuotation.hq_struct> QA_fetch_s2p(grpc::CallOptions options)
      {
        return CallInvoker.AsyncClientStreamingCall(__Method_QA_fetch_s2p, null, options);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override StockHQServiceClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new StockHQServiceClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(StockHQServiceBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_QA_fetch_p2p, serviceImpl.QA_fetch_p2p)
          .AddMethod(__Method_QA_fetch_p2s, serviceImpl.QA_fetch_p2s)
          .AddMethod(__Method_QA_fetch_s2s, serviceImpl.QA_fetch_s2s)
          .AddMethod(__Method_QA_fetch_s2p, serviceImpl.QA_fetch_s2p).Build();
    }

  }
}
#endregion